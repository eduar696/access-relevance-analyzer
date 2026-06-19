def print_terminal_report(results):
    """Muestra el reporte formateado en la terminal."""
    print("\n--- ACCESS RELEVANCE ANALYZER ---")
    if not results:
        print("No se encontraron usuarios de riesgo.")
        return

    for entry in results:
        print(f"User: {entry['username']}")
        print(f"  Level: {entry['risk']['level']} (Score: {entry['risk']['score']})")
        print(f"  Reasons: {', '.join(entry['risk']['reasons'])}")
        print("-" * 20)
