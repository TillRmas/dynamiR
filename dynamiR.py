import win32api
import win32con
import pywintypes

#Crédito a la inteligencia artificial, ella hizo el trabajo.

def obtener_resolucion_nativa():
    # ENUM_REGISTRY_SETTINGS (-2) obtiene la resolución guardada en el registro (la nativa/recomendada)
    nativa = win32api.EnumDisplaySettings(None, win32con.ENUM_REGISTRY_SETTINGS)
    return (nativa.PelsWidth, nativa.PelsHeight)

def cambiar_resolucion(ancho, alto, hz=60):
    print(f"Intentando cambiar a {ancho}x{alto} a {hz}Hz...")
    
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = ancho
    devmode.PelsHeight = alto
    devmode.DisplayFrequency = hz
    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT | win32con.DM_DISPLAYFREQUENCY

    resultado = win32api.ChangeDisplaySettings(devmode, 0)
    
    if resultado == win32con.DISP_CHANGE_SUCCESSFUL:
        print("✅ Cambio exitoso.")
    else:
        print("❌ Error: Resolución no soportada.")

def toggle_resolucion():
    # 1. Detectar resolución actual
    actual = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    ancho_actual = actual.PelsWidth

    # 2. Detectar resolución nativa dinámicamente
    HIGH = obtener_resolucion_nativa()
    
    # 3. Definir tu resolución baja (puedes dejarla fija o calcular un porcentaje)
    LOW = (911, 512)

    print(f"Resolución Nativa detectada: {HIGH[0]}x{HIGH[1]}")

    if ancho_actual == HIGH[0]:
        cambiar_resolucion(LOW[0], LOW[1])
    else:
        cambiar_resolucion(HIGH[0], HIGH[1])

if __name__ == "__main__":

    toggle_resolucion()
