import pwd
import subprocess

def get_all_users():
    """Obtiene una lista de usuarios con su shell y su última conexión."""
    users = []
    for user in pwd.getpwall():
        if user.pw_uid >= 1000 and user.pw_name != "nobody":
            users.append({
                "username": user.pw_name,
                "uid": user.pw_uid,
                "shell": user.pw_shell,
                "last_login": get_last_login(user.pw_name)
            })
    return users

def get_last_login(username):
    """Consulta lastlog para un usuario específico."""
    try:
        # Ejecutamos lastlog para el usuario específico
        result = subprocess.check_output(['lastlog', '-u', username], text=True)
        # lastlog devuelve una cabecera y una línea de datos, tomamos la última
        lines = result.strip().split('\n')
        if len(lines) > 1:
            return lines[1].split(maxsplit=2)[1] # Ajusta según el formato de tu sistema
        return "Nunca"
    except Exception:
        return "Error"

if __name__ == "__main__":
    for u in get_all_users():
        print(f"User: {u['username']} | Last: {u['last_login']}")
