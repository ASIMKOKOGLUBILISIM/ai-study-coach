def generate_study_plan(level, goal, daily_hours):
    subjects = ["Matematik", "Türkçe", "Fen", "İngilizce", "Teknoloji"]
    
    print("\n📚 Kişisel Haftalık Çalışma Planın\n")
    print(f"Seviye: {level}")
    print(f"Hedef: {goal}")
    print(f"Günlük Çalışma Süresi: {daily_hours} saat\n")

    for day in ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]:
        print(f"🔹 {day}:")
        for subject in subjects:
            time = round(daily_hours / len(subjects), 1)
            print(f"   - {subject}: {time} saat")
        print()

print("🤖 AI Study Coach - Mini Demo\n")

level = input("Sınıfın / seviyen: ")
goal = input("Hedefin (ör: sınav başarısı, proje, tekrar): ")
daily_hours = float(input("Günde kaç saat çalışabilirsin?: "))

generate_study_plan(level, goal, daily_hours)
