from math import sqrt

class Estrella():
    """
    Clase que representa una estrella. Sus atributos principales son:

    Atributos:
    - nombre: El nombre de la estrella. (público)
    - masa: La masa de la estrella. (protegido)
    - radio: El radio de la estrella. (protegido)
    - temperaturasuperficial: La temperatura superficial de la estrella. (protegido)
    - distancia: La distancia de la estrella. (protegido)
    - movimientopropio: El movimiento propio de la estrella. (protegido)
    """

    def __init__(self, nombre, masa, radio, temperaturasuperficial, distancia, movimientopropio):
        self.nombre = nombre
        self._masa = masa
        self._radioestrella = radio
        self._teff = temperaturasuperficial
        self._distancia = distancia
        self._movimientopropio = movimientopropio
    
    def luminosidad_total(self):
        """
        Calcula la luminosidad total de la estrella.

        Returns:
        - La luminosidad total de la estrella.
        """
        return 4 * 3.1416 * self._radioestrella**2 * self._teff
    
    def luminosidad_secuencia_principal(self,l_sol, m_sol):
        """
        Calcula la luminosidad de la estrella en la secuencia principal.

        Parámetros:
        - l_sol: La luminosidad del Sol.
        - m_sol: La masa del Sol.

        Returns:
        - La luminosidad de la estrella en la secuencia principal.
        """
        return l_sol * (self._masa / m_sol)**3.5
    
    def temperatura_central(self):
        """
        Calcula la temperatura central de la estrella utilizando una relación simplificada.

        Returns:
        - La temperatura central de la estrella.
        """
        # Se utiliza una relación simplificada entre la temperatura central y la luminosidad y masa de la estrella.
        return self._teff * (self._masa / self.luminosidad_total())**(1/4)
 
