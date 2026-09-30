# Series RLC with Analog PID Control

Analog PID controller (op-amp based) designed to eliminate the step-response overshoot of an
underdamped series RLC circuit, documented as an honest engineering logbook: every result is marked as
calculated, simulated, or pending — no invented placeholder data. First of two related course projects;
the second applies the same PID methodology to a buck converter (see
[BUCK_1](../BUCK_1) — an earlier, IC-based adjustable buck, not the PID-controlled version required for
that follow-up project).

- **Plant:** series RLC, $f_0 \approx$ 5 kHz, $\zeta \approx 0.2$ (clearly underdamped by design)
- **Calculated:** L = 10.13 mH, R = 127.32 Ω, C = 100 nF (fixed) — predicted open-loop overshoot ≈52.7%
- **Goal:** classical PID design (root locus / pole placement) to eliminate that overshoot in closed loop

> ⚠️ **Work in progress.** The plant is fixed and its open-loop overshoot confirmed analytically, but the
> PID gain selection, the op-amp compensator circuit, and the closed-loop SPICE validation are still
> open — see the PDF's `PENDING` boxes for exactly what's outstanding.

## Repository structure

```
docs/         LaTeX document (rlc_pid.tex) + figures
simulation/   LTspice project: schematic (.asc), results (.raw), and log
```

## Document

The report (plant derivation, open-loop transfer function and overshoot prediction, and the outstanding
PID design / simulation work explicitly marked pending) is in
[`docs/rlc_pid.pdf`](docs/rlc_pid.pdf) — compiled and committed, no LaTeX install needed to read it.

Source is [`docs/rlc_pid.tex`](docs/rlc_pid.tex), if you want to edit or recompile it yourself
(`pdflatex`, or [Overleaf](https://www.overleaf.com/)).

## Simulation (LTspice)

Not yet started — planned: open-loop step response (confirming the ~52.7% predicted overshoot),
closed-loop step response with the designed PID, numeric export from the `.raw` file (no visual plot
reading), same methodology as the LM317 and buck (LT8609) projects.

## License

MIT — see [LICENSE](LICENSE).
