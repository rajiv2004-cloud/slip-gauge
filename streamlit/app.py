import streamlit as st
from itertools import combinations

# Default slip gauges
default_gauges = [
    1.005, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.10, 1.11,
    1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.20, 1.21, 1.22, 1.23,
    1.24, 1.25, 1.26, 1.27, 1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34, 1.35,
    1.36, 1.37, 1.38, 1.39, 1.40, 1.41, 1.42, 1.43, 1.44, 1.45, 1.46, 1.47,
    1.48, 1.49, 0.5, 1, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.5, 3, 3.5, 4, 4.5, 5,
    5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
]

def find_combination(target_length, gauges):
    gauges.sort(reverse=True)
    n = len(gauges)
    
    for r in range(1, n + 1):
        for combo in combinations(gauges, r):
            if sum(combo) == target_length:
                return list(combo)
    
    return []

# Streamlit UI
def main():
    st.title("Slip Gauge Combination Calculator")

    # Input for component length
    component_length = st.number_input("Enter the component length:", min_value=0.0, step=0.01, format="%.2f")

    # Input for additional slip gauges
    additional_gauges = st.text_input("Enter additional slip gauges (comma-separated):")
    
    gauges = default_gauges.copy()
    
    if additional_gauges:
        try:
            additional_gauges = [float(x) for x in additional_gauges.split(',')]
            gauges.extend(additional_gauges)
        except ValueError:
            st.error("Invalid input for additional gauges. Please enter numeric values separated by commas.")
            return
    
    if st.button("Calculate"):
        if component_length > 0:
            required_gauges = find_combination(component_length, gauges)
            if required_gauges:
                st.success(f"Required slip gauges: {', '.join(map(str, required_gauges))} = {sum(required_gauges)}")
            else:
                st.warning("No combination of slip gauges can achieve the exact component length.")
        else:
            st.error("Please enter a valid component length.")

if __name__ == "__main__":
    main()
