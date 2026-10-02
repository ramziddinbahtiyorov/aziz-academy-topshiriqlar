# choice
# start -> "Started"
# stop -> "Stopped"
# pause -> "Paused"
# aks holda "Unknown command"
choice = input()
if choice == "start":
    print("Started")
elif choice == "Stop":
    print("Stopped")
elif choice == "Paused":
    print("Paused")
else:
    print("Unknown command")