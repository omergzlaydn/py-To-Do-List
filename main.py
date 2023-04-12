tasks = {
    "Görev 1": False,
    "Görev 2": True,
    "Görev 3": False
}

def add_task():
    task_name = input("Eklemek istediğiniz görev nedir? ")
    tasks[task_name] = False
    print("Görev eklendi.")

def list_tasks():
    for task_name, completed in tasks.items():
        status = "tamamlandı" if completed else "tamamlanmadı"
        print(f"{task_name}: {status}")

def complete_task():
    task_name = input("Tamamladığınız görevin adı nedir? ")
    if task_name not in tasks:
        print("Görev bulunamadı.")
    else:
        tasks[task_name] = True
        print("Görev tamamlandı.")

def main():
    while True:
        print("""
        1. Görev ekle
        2. Görevleri listele
        3. Görev tamamla
        4. Çıkış
        """)
        choice = input("Seçiminiz (1/2/3/4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
