function toggleSection() {
  var x = document.getElementById("menuL");
  x.hidden = true;
}


let mode = 'finance';
const endpoints = { 'finance': '/api/v1/basic-metrics', 'risk': '/api/v1/risk-metrics', 'portfolio': '/api/v1/portfolio-metrics' };

function setMode(m) {
  mode = m;
  const container = document.getElementById('inputs-container');
  document.querySelectorAll('nav button').forEach(b => {
    b.className = "px-4 py-1.5 rounded text-xs font-bold transition " +
      (b.id === 'btn-' + m ? "bg-blue-600 text-white" : "text-slate-500 hover:text-slate-300");
  });

  if (m === 'finance') {
    container.innerHTML = `
                    <div class="space-y-1">
                        <label class="text-[9px] font-bold text-slate-500 uppercase">Target Ticker</label>
                        <input id="t1" value="PETR4.SA" class="w-full bg-slate-900 border border-slate-700 rounded p-2 text-xs text-white outline-none">
                    </div>
                    <div class="space-y-1">
                        <label class="text-[9px] font-bold text-slate-500 uppercase">Benchmark Reference</label>
                        <input id="t2" value="^BVSP" class="w-full bg-slate-900 border border-slate-700 rounded p-2 text-xs text-white outline-none">
                    </div>`;
  } else if (m === 'risk') {
    container.innerHTML = `
                    <div class="space-y-1">
                        <label class="text-[9px] font-bold text-slate-500 uppercase">Analysis Asset</label>
                        <input id="t1" value="PETR4.SA" class="w-full bg-slate-900 border border-slate-700 rounded p-2 text-xs text-white outline-none">
                    </div>

                    <div class="flex items-center justify-between bg-slate-900/50 p-3 rounded border border-slate-800">
                        <label class="text-[10px] font-bold text-slate-400 uppercase cursor-pointer">
                            Short Position Mode
                        </label>
                        <input id="short-check" type="checkbox"
                            class="w-4 h-4 rounded border-slate-700 bg-slate-800 text-blue-500 focus:ring-0">
                    </div>
                `;
  } else {
    container.innerHTML = `
                    <div class="space-y-1">
                        <label class="text-[9px] font-bold text-slate-500 uppercase">Portfolio Assets (CSV)</label>
                        <textarea id="t1" class="w-full bg-slate-900 border border-slate-700 rounded p-2 text-xs text-white outline-none h-20">PETR4.SA, VALE3.SA, ITUB4.SA, BBAS3.SA</textarea>
                    </div>`;
  }
}

async function executar() {
  const isAiChecked = document.getElementById('ai-check').checked;
  const payload = { start_date: document.getElementById('start').value, end_date: document.getElementById('end').value, ai_analysis: isAiChecked };
  document.getElementById('empty-state').classList.add('hidden');
  document.getElementById('dashboard').classList.remove('hidden');

  if (mode === 'finance') { payload.ticker = document.getElementById('t1').value; payload.benchmark = document.getElementById('t2').value; }
  else if (mode === 'risk') {
    payload.ticker = document.getElementById('t1').value;
    payload.short = document.getElementById('short-check')?.checked || false;
  }
  else { payload.tickers = document.getElementById('t1').value.split(',').map(t => t.trim()); }

  document.getElementById('ia-badge').innerText = "Processing...";
  document.getElementById('ia-content').innerText = "Initiating Quantum Engine Analysis...";

  try {
    const response = await fetch(`http://127.0.0.1:8002${endpoints[mode]}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'x-api-key': 'vibe_08b699e0f7b9e06db19974ea06efe444' },
      body: JSON.stringify(payload)
    });
    const data = await response.json();

    document.getElementById('raw-log').innerText = JSON.stringify(data, null, 2);
    renderDashboard(data);
  } catch (e) {
    document.getElementById('ia-content').innerText = "CONNECTION_ERROR: Check server status at port 8001.";
  }
}

function renderDashboard(data) {

  const grid = document.getElementById('metrics-grid');
  const secondary = document.getElementById('secondary-metrics');
  const iaContent = document.getElementById('ia-content');
  const manifest = document.getElementById('manifest-content');

  const portfolioTableContainer = document.getElementById('portfolio-table-container');
  portfolioTableContainer.innerHTML = '';
  portfolioTableContainer.classList.add('hidden');

  grid.innerHTML = '';
  secondary.innerHTML = '';

  function percent(v) {
    if (v === undefined || v === null) return '-';
    return (v * 100).toFixed(2) + '%';
  }

  function number(v, decimals = 4) {
    if (v === undefined || v === null) return '-';
    return v.toFixed(decimals);
  }

  // =====================================================
  // ===================== PORTFOLIO =====================
  // =====================================================
  if (mode === 'portfolio') {
    grid.className = "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4";

    const portfolio = data.results?.portfolio || {};
    const corr = data.results?.correlation_matrix || {};
    const individual = data.results?.individual_metrics || {};

    // ===== PRINCIPAIS
    const mainMetrics = [
      { label: 'Expected Return', value: percent(portfolio.expected_return), glow: true },
      { label: 'CAGR', value: percent(portfolio.cagr) },
      { label: 'Volatility', value: percent(portfolio.volatility) },
      { label: 'Sharpe Ratio', value: number(portfolio.sharpe, 3) }
    ];

    mainMetrics.forEach(m => {
      grid.innerHTML += `
                <div class="metric-card p-6 rounded-xl">
                    <div class="text-[10px] font-bold text-slate-500 uppercase mb-2">${m.label}</div>
                    <div class="text-3xl font-black mono ${m.glow ? 'glow-green' : 'text-white'}">
                        ${m.value}
                    </div>
                </div>`;
    });

    // ===== CORRELAÇÃO MÉDIA
    let corrValues = [];
    Object.keys(corr).forEach(a => {
      Object.keys(corr[a]).forEach(b => {
        if (a !== b) corrValues.push(corr[a][b]);
      });
    });

    const avgCorr = corrValues.length
      ? corrValues.reduce((a, b) => a + b, 0) / corrValues.length
      : null;

    secondary.innerHTML += `
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
                <span class="text-[10px] text-slate-500 font-bold uppercase">Avg Correlation</span>
                <span class="text-xs mono font-bold text-blue-400">${number(avgCorr, 3)}</span>
            </div>
        `;

    // ===== TABELA FULL WIDTH

    if (individual.cagr) {

      portfolioTableContainer.classList.remove('hidden');

      const tickers = Object.keys(individual.cagr);

      let tableHTML = `
        <div class="metric-card rounded-xl overflow-hidden">
            <div class="bg-slate-800/50 px-4 py-3 border-b border-slate-700">
                <span class="text-[10px] font-bold text-blue-400 uppercase tracking-widest">
                    Portfolio Assets Breakdown
                </span>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-xs mono">
                    <thead class="bg-slate-900">
                        <tr>
                            <th class="p-4 text-left">Asset</th>
                            <th class="p-4 text-right">CAGR</th>
                            <th class="p-4 text-right">Sharpe</th>
                            <th class="p-4 text-right">Volatility</th>
                            <th class="p-4 text-right">Max DD</th>
                        </tr>
                    </thead>
                    <tbody>
    `;

      tickers.forEach(ticker => {
        tableHTML += `
            <tr class="border-t border-slate-800 hover:bg-slate-900/40 transition">
                <td class="p-4 font-bold text-slate-300">${ticker}</td>
                <td class="p-4 text-right">${percent(individual.cagr[ticker])}</td>
                <td class="p-4 text-right">${number(individual.sharpe?.[ticker], 3)}</td>
                <td class="p-4 text-right">${percent(individual.volatility?.[ticker])}</td>
                <td class="p-4 text-right">${percent(individual.max_drawdown?.[ticker])}</td>
            </tr>
        `;
      });

      tableHTML += `
                    </tbody>
                </table>
            </div>
        </div>
    `;

      portfolioTableContainer.innerHTML = tableHTML;
    }

  }

  else if (mode === 'risk') {
    grid.className = "grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-4";

    const res = data.results || {};

    const mainMetrics = [
      { label: 'VaR 95%', value: percent(res.var_95) },
      { label: 'VaR 98%', value: percent(res.var_98) },
      { label: 'VaR 99%', value: percent(res.var_99), glow: true },
      { label: 'VaR 99.9%', value: percent(res.var_99_9) },
      { label: 'Worst Day', value: percent(res.worst_day) }
    ];

    mainMetrics.forEach(m => {
      grid.innerHTML += `
            <div class="metric-card p-6 rounded-xl">
                <div class="text-[10px] font-bold text-slate-500 uppercase mb-2">${m.label}</div>
                <div class="text-3xl font-black mono ${m.glow ? 'glow-blue' : 'text-white'}">
                    ${m.value}
                </div>
            </div>`;
    });

    const subMetrics = [
      { label: 'CVaR 95%', value: percent(res.cvar_95) },
      { label: 'CVaR 98%', value: percent(res.cvar_98) },
      { label: 'CVaR 99%', value: percent(res.cvar_99) },
      { label: 'CVaR 99.9%', value: percent(res.cvar_99_9) },
      { label: 'Daily Std Dev', value: percent(res.daily_std) },
      { label: 'Z-Score Worst Day', value: number(res.z_score_worst, 2) }
    ];

    subMetrics.forEach(m => {
      secondary.innerHTML += `
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
                <span class="text-[10px] text-slate-500 font-bold uppercase">${m.label}</span>
                <span class="text-xs mono font-bold text-blue-400">${m.value}</span>
            </div>`;
    });

  }

  else if (mode === 'finance') {
    grid.className = "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4";

    const res = data.results || {};

    const mainMetrics = [
      { label: 'Total Return', value: percent(res.total_return), glow: true },
      { label: 'Benchmark Return', value: percent(res.benchmark_return) },
      { label: 'Annualized Volatility', value: percent(res.volatility_ann) },
      { label: 'Max Drawdown', value: percent(res.max_drawdown) }
    ];

    mainMetrics.forEach(m => {
      grid.innerHTML += `
            <div class="metric-card p-6 rounded-xl">
                <div class="text-[10px] font-bold text-slate-500 uppercase mb-2">${m.label}</div>
                <div class="text-3xl font-black mono ${m.glow ? 'glow-green' : 'text-white'}">
                    ${m.value}
                </div>
            </div>`;
    });

    const subMetrics = [
      { label: 'CAGR', value: percent(res.cagr) },
      { label: 'Volatility (Daily)', value: percent(res.volatility_daily) },
      { label: 'Sharpe (Annual)', value: number(res.sharpe_ann, 3) },
      { label: 'Sharpe (Period)', value: number(res.sharpe_period, 3) },
      { label: 'Beta vs Benchmark', value: number(res.beta, 3) },
      { label: 'Correlation', value: number(res.correlation, 3) }
    ];

    subMetrics.forEach(m => {
      secondary.innerHTML += `
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
                <span class="text-[10px] text-slate-500 font-bold uppercase">${m.label}</span>
                <span class="text-xs mono font-bold text-blue-400">${m.value}</span>
            </div>`;
    });


  }

  // =====================================================
  // ======================= AI ===========================
  // =====================================================

  iaContent.innerText = data.ai_analysis ||
    "AI analysis not requested. Enable AI Engine to generate insights.";

  document.getElementById('ia-badge').innerText =
    data.ai_analysis ? "Analysis Ready" : "Standby";

  renderEngineSpecification(data);

}

function renderEngineSpecification(data) {

  const manifest = document.getElementById('manifest-content');
  const spec = data.engine_specification || {};
  const parameters = data.parameters || {};
  const requestId = data.request_id || '-';

  let html = `
        <div class="space-y-3">
            <div class="border-b border-slate-800 pb-2">
                <div class="text-blue-400 font-bold">REQUEST</div>
                <div>> ID:<span class="font-bold text-slate-300 mb-1"> ${requestId}</span></div>
                <div>> MODE:<span class="font-bold text-slate-300 mb-1"> ${mode.toUpperCase()}</span></div>
                <div>> PERIOD:<span class="font-bold text-slate-300 mb-1"> ${parameters.start_date || '-'} → ${parameters.end_date || '-'}</span></div>
            </div>

            <div>
                <div class="text-blue-400 font-bold mb-2">ENGINES EXECUTED</div>
    `;

  Object.keys(spec).forEach(engineKey => {

    const block = spec[engineKey];
    const manifestData = block?.manifest || {};
    const assumptions = manifestData.assumptions;

    html += `
            <div class="mb-5 border border-slate-800 p-3 rounded bg-slate-900/40">
                <div class="font-bold text-blue-400 mb-1">${engineKey}</div>
                <div>> ENGINE:<span class="font-bold text-slate-300 mb-1"> ${manifestData.engine || block.engine || '-'}</span></div>
                <div>> VERSION:<span class="font-bold text-slate-300 mb-1"> ${manifestData.version || manifestData.engine_version || '-'}</span></div>
                <div>> FORMULA:<span class="font-bold text-slate-300 mb-1"> ${manifestData.formula_version || '-'}</span></div>
                <div>> DATAFRAME:<span class="font-bold text-slate-300 mb-1"> ${manifestData.dataframe_version || '-'}</span></div>
                <div>> EFFECTIVE:<span class="font-bold text-slate-300 mb-1"> ${manifestData.effective_date || block.effective_date || '-'}</span></div>
                <div><span>&nbsp;</span></div>
        `;

    // ============================
    // ASSUMPTIONS (DINÂMICO)
    // ============================

    if (assumptions) {

      html += `<div class="font-bold text-blue-400 mb-1">Assumptions</div>`;

      if (typeof assumptions === "object") {

        Object.keys(assumptions).forEach(key => {
          html += `<div>> ${key}:<span class="font-bold text-slate-300 mb-1"> ${assumptions[key]}</span></div>`;
        });

      } else {

        html += `<div>> ${assumptions}</div>`;

      }
    }

    html += `</div>`;
  });

  html += `</div></div>`;

  manifest.innerHTML = html;
}
