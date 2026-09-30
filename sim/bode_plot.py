import numpy as np
from scipy import signal
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

f0 = 5000.0
wn = 2*np.pi*f0
zeta = 0.2

Kp = 27.87
Ki = 455905.0
Kd = 3.114e-4

G_num = [wn**2]
G_den = [1, 2*zeta*wn, wn**2]
C_num = [Kd, Kp, Ki]
C_den = [1, 0]

L_num = np.polymul(C_num, G_num)
L_den = np.polymul(C_den, G_den)
L_sys = signal.TransferFunction(L_num, L_den)

w = np.logspace(-1, 7, 4000)
w, mag, phase = signal.bode(L_sys, w)

n = max(len(L_num), len(L_den))
Ln = np.pad(L_num, (n-len(L_num), 0))
Ld = np.pad(L_den, (n-len(L_den), 0))
T_sys = signal.TransferFunction(Ln, Ln+Ld)
wT, magT, phaseT = signal.bode(T_sys, w)

def crossings(x, y, level):
    idx = np.where(np.diff(np.sign(y - level)))[0]
    out = []
    for i in idx:
        x0,x1,y0,y1 = x[i],x[i+1],y[i],y[i+1]
        xc = x0 + (level-y0)*(x1-x0)/(y1-y0)
        out.append(xc)
    return out

gc = crossings(w, mag, 0.0)
wc = gc[0]
ph_at_wc = np.interp(np.log10(wc), np.log10(w), phase)
pm = 180+ph_at_wc

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0,0].semilogx(w, mag); axes[0,0].axhline(0, color='gray', lw=0.5)
axes[0,0].axvline(wc, color='r', ls='--', lw=0.9)
axes[0,0].set_title("Open-loop L(s)=C(s)G(s) -- Magnitude"); axes[0,0].set_ylabel("dB")
axes[0,0].grid(True, which="both", alpha=0.3)

axes[1,0].semilogx(w, phase); axes[1,0].axhline(-180, color='gray', lw=0.5)
axes[1,0].axvline(wc, color='r', ls='--', lw=0.9, label=f"PM = {pm:.1f} deg @ {wc:.0f} rad/s")
axes[1,0].set_title("Open-loop L(s)=C(s)G(s) -- Phase"); axes[1,0].set_ylabel("deg"); axes[1,0].set_xlabel("rad/s")
axes[1,0].legend(fontsize=9, loc='lower right')
axes[1,0].grid(True, which="both", alpha=0.3)

axes[0,1].semilogx(wT, magT); axes[0,1].axhline(0, color='gray', lw=0.5); axes[0,1].axhline(-3, color='g', ls=':', lw=0.8, label="-3dB")
axes[0,1].set_title("Closed-loop T(s) -- Magnitude"); axes[0,1].set_ylabel("dB")
axes[0,1].legend(fontsize=9)
axes[0,1].grid(True, which="both", alpha=0.3)

axes[1,1].semilogx(wT, phaseT)
axes[1,1].set_title("Closed-loop T(s) -- Phase"); axes[1,1].set_ylabel("deg"); axes[1,1].set_xlabel("rad/s")
axes[1,1].grid(True, which="both", alpha=0.3)

plt.tight_layout()
out = "/home/tostada105/Proyects/Escuela/PCBs/RLC_PID/docs/figures/bode_plot.png"
plt.savefig(out, dpi=150)
print("saved", out)
print(f"wc={wc:.1f} rad/s, PM={pm:.2f} deg")
