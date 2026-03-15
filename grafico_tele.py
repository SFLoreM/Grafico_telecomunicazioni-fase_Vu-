import numpy as np
import matplotlib.pyplot as plt

# Dati della tua tabella (Punto 3)
frequenze = np.array([30e3, 270e3, 800e3, 2e6, 5e6, 70e6])
v_uscita = np.array([3.36, 3.40, 2.12, 0.071, 0.232, 0.124]) # Valori in Volt (V_u)
fase = np.array([0.00, 11.66, 25.34, 99.36, 176.40, 181.44]) # Valori in gradi (phi)

# Creazione dei grafici
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# 1. Grafico Tensione di Uscita (V_u)
ax1.plot(frequenze, v_uscita, 'o-', color='blue', linewidth=2, markersize=8, label='$V_u$ misurata')
ax1.set_xscale('log') # Scala logaritmica per le frequenze come da lavagna
ax1.set_title('Andamento della Tensione di Uscita ($V_u$) e della Fase', fontsize=14, fontweight='bold')
ax1.set_ylabel('Tensione di Uscita $V_u$ [V]', fontsize=12)
ax1.grid(True, which="both", ls="--", alpha=0.6)
ax1.legend()

# 2. Grafico Fase (phi)
ax2.plot(frequenze, fase, 's-', color='red', linewidth=2, markersize=8, label='Sfasamento $\phi$')
ax2.set_xscale('log')
ax2.set_xlabel('Frequenza [Hz]', fontsize=12)
ax2.set_ylabel('Sfasamento $\phi$ [Gradi]', fontsize=12)
ax2.grid(True, which="both", ls="--", alpha=0.6)
ax2.legend()

plt.tight_layout()
plt.savefig('grafico_vu_fase.png', dpi=300)
plt.show()