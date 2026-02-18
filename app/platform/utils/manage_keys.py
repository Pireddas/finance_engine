# app\platform\utils\manage_keys.py
# python -m app.platform.utils.manage_keys

<<<<<<< HEAD
import sqlite3, secrets, hashlib, os, psycopg2
from psycopg2.extras import RealDictCursor
from app.application.config import settings

# Carregando configurações
DB_DIR = settings.DB_DIR
DB_PATH = settings.DB_PATH
DB_TYPE = settings.DB_TYPE
POSTGRES_URL = settings.POSTGRES_URL

def get_connection():
    """Retorna a conexão correta baseada no tipo de banco."""
    if DB_TYPE == "postgresql":
        # Usamos client_encoding para evitar o erro de Unicode no Windows
        conn = psycopg2.connect(POSTGRES_URL, client_encoding='utf8')
        return conn
    else:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

def init_db():
=======
import sqlite3, secrets, hashlib, os
from app.application.config import settings

DB_DIR = settings.DB_DIR
DB_PATH = settings.DB_PATH

def init_db():
    # 2. Garante a criação da pasta 'database' dentro de 'src'
>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
        print(f"📁 Pasta de governança criada em: {DB_DIR}")

<<<<<<< HEAD
    conn = get_connection()
    cursor = conn.cursor()
    
    if DB_TYPE == "sqlite":
=======
    if settings.DB_TYPE == "sqlite":
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS api_keys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key_hash TEXT UNIQUE NOT NULL,
                owner TEXT NOT NULL,
                active INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
<<<<<<< HEAD
    else:
        # Postgres usa SERIAL para autoincremento
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS api_keys (
                id SERIAL PRIMARY KEY,
                key_hash TEXT UNIQUE NOT NULL,
                owner TEXT NOT NULL,
                active INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    
    conn.commit()
    conn.close()
=======
        conn.commit()
        conn.close()
    elif settings.DB_TYPE == "postgresql":
        # Implementar criação de tabela para PostgreSQL se necessário
        pass
>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383

def create_key():
    owner = input("\n👤 Nome do Proprietário (Owner): ").strip()
    if not owner: return print("❌ Erro: Nome é obrigatório.")
    
    raw_key = f"vibe_{secrets.token_hex(16)}"
    key_hash = hashlib.sha256(raw_key.encode()).hexdigest()
    
<<<<<<< HEAD
    conn = get_connection()
    cursor = conn.cursor()
    
    # Placeholder muda conforme o banco: ? para SQLite, %s para Postgres
    query = "INSERT INTO api_keys (key_hash, owner) VALUES (?, ?)" if DB_TYPE == "sqlite" else \
            "INSERT INTO api_keys (key_hash, owner) VALUES (%s, %s)"
    
    try:
        cursor.execute(query, (key_hash, owner))
        conn.commit()
        print(f"\n✅ Chave criada para: {owner}")
        print(f"🔑 API KEY: {raw_key}")
        print("⚠️  AVISO: Guarde esta chave! Ela não pode ser recuperada.\n")
    finally:
        conn.close()

def list_keys():
    print("\n--- CHAVES CADASTRADAS ---")
    conn = get_connection()
    
    # No Postgres, usamos RealDictCursor para simular o sqlite3.Row
    cursor = conn.cursor(cursor_factory=RealDictCursor) if DB_TYPE == "postgresql" else conn.cursor()
    
    try:
        cursor.execute("SELECT id, owner, active, created_at FROM api_keys ORDER BY id DESC")
=======
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO api_keys (key_hash, owner) VALUES (?, ?)", (key_hash, owner))
    
    print(f"\n✅ Chave criada para: {owner}")
    print(f"🔑 API KEY: {raw_key}")
    print("⚠️  AVISO: Guarde esta chave! Ela não pode ser recuperada.\n")

def list_keys():
    print("\n--- CHAVES CADASTRADAS ---")
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute("SELECT id, owner, active, created_at FROM api_keys")
>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383
        rows = cursor.fetchall()
        
        if not rows:
            print("Nenhuma chave encontrada.")
            return

        print(f"{'ID':<4} | {'OWNER':<30} | {'STATUS':<11} | {'DATA CRIAÇÃO'}")
        print("-" * 75)
        for row in rows:
<<<<<<< HEAD
            # Acesso uniforme via chave (funciona para sqlite3.Row e RealDictCursor)
            status = "✅ ATIVA" if row['active'] == 1 else "❌ INATIVA"
            print(f"{row['id']:<4} | {row['owner']:<30} | {status:<10} | {row['created_at']}")
    finally:
        conn.close()
=======
            status = "✅ ATIVA" if row['active'] == 1 else "❌ INATIVA"
            print(f"{row['id']:<4} | {row['owner']:<30} | {status:<10} | {row['created_at']}")
>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383
    print("-" * 75)

def toggle_key_status(status: int):
    action = "Ativar" if status == 1 else "Cancelar/Inativar"
    key_id = input(f"\nDigite o ID da chave que deseja {action}: ").strip()
    
<<<<<<< HEAD
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "UPDATE api_keys SET active = ? WHERE id = ?" if DB_TYPE == "sqlite" else \
            "UPDATE api_keys SET active = %s WHERE id = %s"
    
    try:
        cursor.execute(query, (status, key_id))
        conn.commit()
=======
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("UPDATE api_keys SET active = ? WHERE id = ?", (status, key_id))
>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383
        if cursor.rowcount > 0:
            print(f"✅ Sucesso: Chave {key_id} atualizada.")
        else:
            print(f"❌ Erro: ID {key_id} não encontrado.")
<<<<<<< HEAD
    finally:
        conn.close()
=======
>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383

def main_menu():
    init_db() 
    while True:
<<<<<<< HEAD
        print(f"\n=== 🛡️ GESTAO DE CHAVES API ({DB_TYPE.upper()}) ===")
=======
        print("\n=== 🛡️ GESTAO DE CHAVES API ===")
>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383
        print("1. Gerar Nova Chave")
        print("2. Listar Todas as Chaves")
        print("3. Inativar/Cancelar Chave")
        print("4. Reativar Chave")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1": create_key()
        elif opcao == "2": list_keys()
        elif opcao == "3": toggle_key_status(0)
        elif opcao == "4": toggle_key_status(1)
        elif opcao == "0": break
        else: print("Opção inválida.")

if __name__ == "__main__":
<<<<<<< HEAD
    main_menu()
=======
    main_menu()
>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383
