def adjectival_equivalent(percent):
   if 96 <= percent <= 100:
      return 1.00, "EXCELLENT"
   elif 90 <= percent < 96:
      return 1.25, "VERY GOOD"
   elif 84 <= percent < 90
      return 1.50, "VERY GOOD"
   elif 78 <= percent < 84:
      return 1.75, "GOOD"
   elif 72 <= percent < 78
      return 2.00, "GOOD"
   elif 66 <= percent < 72:
      return 2.25, "SATISFACTORY"
   elif 60 <= percent < 66:
      return 2.50, "SATISFACTORY"
   elif 55 <= percent < 60:
      return 2.75, "FAIR"
   elif 50 <= percent < 55:
      return 3.00, "FAIR"
   elif 40 <= percent < 50:
      return 4.00, "FAILED ON CONDITION"
   else:
      return 5.00, "FAILED"

      def compute_final_quarter_grade():
         print("Final Quarter Grade Calculator")

         q1 = float(input("Enter Tentative Q1 tentative/raw grade: "))
         q2_tent = float(input("Enter Tentative Q2 grade: "))
         q3_tent = float(input("Enter Tentative Q3 grade: "))
         q4_tent = float(input("Enter Tentative Q4 grade: "))

         q2 = (q1 + 2 * q2_tent) / 3
         q3 = (q1 + 2 * q3_tent) / 3
         q4 = (q1 + 2 * q4_tent) / 3

         equivalent, adjective = adjectival_equivalent(q4)

         print("\nComputed Grades")
         print(f"Q2 Final Grade: {q2:.2f}")
         print(f"Q3 Final Grade: {q3:.2f}")
         print(f"Q4 Final Grade: {q4:.2f}")
         print(f"Fina Quarter Grade Equivalent: {equivalent:.2f}")
         print(f"Adjectival Equivalent: {adjective}")

compute_final_quarter_grade()