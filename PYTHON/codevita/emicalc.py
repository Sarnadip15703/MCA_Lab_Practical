def calculate_total_payment():
    principal = float(input("Enter Principle: ").strip())
    tenure_years = int(input("Enter Tenure: ").strip())
    
    bank_sums = []

    for _ in range(2):
        num_slabs = int(input(f"Enter number of slabs for Bank {chr(_+65)}: ").strip())
        total_sum = 0
        
        for i in range(num_slabs):
            slab_period, slab_rate = map(float, input("Enter slab_period in years, slab_rate in annual percentage: ").split())
            
            monthly_rate = (slab_rate / 100) / 12
            total_months = tenure_years * 12
            
            emi = (principal * monthly_rate) / (1 - (1 / pow(1 + monthly_rate, total_months)))
            
            total_sum += emi * (slab_period * 12)
        
        bank_sums.append(total_sum)

    if bank_sums[0] < bank_sums[1]:
        print("Bank A")
    else:
        print("Bank B")
        
calculate_total_payment()