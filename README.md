# f(T)-CLASS 
**Cosmic Linear Anisotropy Solving System for Modified Teleparallel Gravity**

Authors: Rebecca Briffa, Carlos Garcia Boiza, Jackson Said, Jurgen Mifsud, Mariam Bouhmadi López, Emmanuel Saridakis

This repository contains a modified version of the **CLASS** code, specifically adapted to study cosmological evolution within the framework of **$f(T)$ gravity**. This version implements the background and linear perturbation equations for modified teleparallel gravity models - currently for the power law model $f(T) = -T + \alpha T^{\beta}$

---

##  Overview
Standard CLASS (developed by Julien Lesgourgues and Thomas Tram) solves the evolution of linear perturbations in the Universe. **f(T)-CLASS** extends this functionality to:
* **Background Evolution:** Solves the modified Friedmann equations for $f(T)$ models.
* **Linear Perturbations:** Includes the specific contributions of $f(T)$ teleparallel gravity to the Einstein-Boltzmann system.

---
##  Prerequisites

To use this code, we highly suggest to first have the standard cosmology stack installed:

1. **CLASS (Original):** Familiarity with the [official CLASS repository](https://github.com/lesgourg/class_public) is recommended.
2. **Cobaya:** Install the Bayesian sampler [official Cobaya repository](https://github.com/CobayaSampler/cobaya).
3. **Verification:** Use the documentation from the official repositories above to ensure both CLASS and Cobaya are working correctly on your system before proceeding.
4. **f(T) CLASS** Download the code from the webpage and unpack the archive, or clone it. Go to the class directory (cd f_T_CLASS) and compile (make clean; make class).

---
## Usage 
To run the code with $f(T)$ gravity, you must define specific model parameters in your .ini file (for CLASS) or .yaml file (for Cobaya).

In this implementation, the parameter param_b refers to the exponent $\beta$ in the power-law functional form. 

To ensure the $f(T)$ logic is triggered correctly, you must set:
- Omega_Lambda: 0
- fluid_equation_of_state: "FT"
- param_b: b
- gauge: "synchronous"

For detailed implementation examples, please refer to:
- fT_example.py: For running f(T)-CLASS standalone using python.
- fT-example.yaml: For running runs within the Cobaya framework.

---
## Using the code
You can use f(T)-CLASS freely. If you use this code in your publications, please acknowledge its usage and also cite the following:
- CLASS II: Approximation schemes – arXiv:1104.2933
- Cobaya (if used): Please cite the pre-print arXiv:2005.05290 and its ASCL record, ascl:1910.019.
