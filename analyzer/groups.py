import grp

# Lista de grupos que consideramos de riesgo o privilegiados
PRIVILEGED_GROUPS = {'sudo', 'docker', 'lxd', 'libvirt', 'adm', 'wheel'}

def get_user_privileged_groups(username):
    """
    Busca a qué grupos privilegiados pertenece un usuario.
    Retorna una lista de grupos encontrados.
    """
    user_groups = []
    # Obtenemos todos los grupos del sistema
    all_groups = grp.getgrall()
    
    for group in all_groups:
        if group.gr_name in PRIVILEGED_GROUPS:
            if username in group.gr_mem:
                user_groups.append(group.gr_name)
    
    return user_groups

if __name__ == "__main__":
    # Prueba rápida
    # Cambia 'eduar' por tu usuario si quieres probar
    print(f"Grupos privilegiados de eduar: {get_user_privileged_groups('eduar')}")
