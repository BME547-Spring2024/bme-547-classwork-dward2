weight = 20 / 2.205
dosage = weight * 30

print("CORRECT DOSAGE")
print("For a patient weighing {:.1f} kg,".format(round(weight, 1)))
print("  the correct dosage is {:.1f} mg the first day".format(round(dosage,
                                                                     1)))
