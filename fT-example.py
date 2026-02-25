from classy import Class
import numpy as np

def run(b: float) -> None:
    print(f"\n=== trying b = {b:.1f} ===")
    c = Class()
    c.set({
        "output": "mPk",
        "z_pk": "0,1,5",
        "P_k_max_1/Mpc": 1.0,
        "omega_b": 0.022,
        "omega_cdm": 0.12,
        "h": 0.67,
        "A_s": 2.1e-9,
        "n_s": 0.96,
        "tau_reio": 0.055,
        "Omega_k": 0,
        "Omega_Lambda": 0,
        "fluid_equation_of_state": "FT",
        "param_b": b,
        "gauge": "synchronous",
        "use_ppf": "no",
        "perturbations_integration_stepsize": 0.01,
        "tol_perturbations_integration": 1e-6,
    })
    c.compute()

    print("H0 =", c.h() * 100)
    print("Omega_m =", c.Omega_m())
    print("P(k,z=0):")
    for kk in [1e-4, 1e-3, 1e-2, 1e-1]:
        print(f" k={kk:10.4e} P={c.pk_lin(kk, 0):.5e}")

    c.struct_cleanup()
    c.empty()

if __name__ == "__main__":
    # sweep b from -1.0 to 1.0 in steps of 0.1
    for b in np.linspace(-1.0, 1.0, 21):
        try:
            run(float(b))
        except Exception as e:
            print(f"\n=== trying b = {b:.1f} ===")
            print("FAILED:", e)

