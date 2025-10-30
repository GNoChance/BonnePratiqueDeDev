import logging
from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@dataclass
class Task:
    """Représente une tache unique dans la liste TODO."""
    id: int
    description: str
    completed: bool = False
    created_at: datetime = datetime.now()

class TodoManager:
    """Gere les opérations de la liste TODO."""
    
    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self.next_id: int = 1
        logging.info("TodoManager initialisé")

    def AjouterTache(self, description: str) -> bool:
        if not description.strip():
            logging.error("Tentative d'ajout d'une tâche vide")
            return False
        
        task = Task(id=self.next_id, description=description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        logging.info(f"Tâche ajoutee: {description}")
        return True

    def ListerTaches(self) -> List[Task]:
        return list(self.tasks.values())

    def MarquerTacheFinie(self, task_id: int) -> bool:
        if task_id not in self.tasks:
            logging.error(f"Tentative de marquage d'une tâche inexistante {task_id}")
            return False
        
        self.tasks[task_id].completed = True
        logging.info(f"Tâche {task_id} marquee comme terminée")
        return True

    def SupprimerTache(self, task_id: int) -> bool:
        if task_id not in self.tasks:
            logging.error(f"Tentative de suppression d'une tâche inexistante {task_id}")
            return False
        
        del self.tasks[task_id]
        logging.info(f"Tâche {task_id} supprimée")
        return True

def AfficherMenu():
    print("\n=== Gestionnaire de Liste TODO ===")
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Marquer une tâche comme terminée")
    print("4. Supprimer une tâche")
    print("5. Quitter")
    return input("Choisissez une option (1-5): ")

def main():
    """
    Point d'entrée principal du gestionnaire de tâches.
    Cette fonction gère la boucle principale du programme qui permet à l'utilisateur
    d'interagir avec le gestionnaire de tâches via un menu. Les opérations disponibles sont:
    - Ajouter une nouvelle tâche
    - Lister les tâches existantes
    - Marquer une tâche comme terminée
    - Supprimer une tâche
    - Quitter l'application
    La fonction gère également les erreurs d'entrée utilisateur et enregistre
    les événements importants dans les logs.
    Returns:
        None
    Raises:
        ValueError: Si l'utilisateur entre un ID de tâche non numérique
    """
    todo_manager = TodoManager()
    
    while True:
        user_choice = AfficherMenu()
        
        try:
            if user_choice == "1":
                task_description = input("Entrez la description de la tâche: ")
                if todo_manager.AjouterTache(task_description):
                    print("Tâche ajoutée avec succès!")
                else:
                    print("Erreur: La description de la tâche ne peut pas être vide")
                    
            elif user_choice == "2":
                current_tasks = todo_manager.ListerTaches()
                if not current_tasks:
                    print("Aucune tâche trouvée.")
                else:
                    print("\nTâches actuelles:")
                    for task in current_tasks:
                        status = "✓" if task.completed else " "
                        print(f"[{status}] {task.id}. {task.description}")
                        
            elif user_choice == "3":
                task_id = int(input("Entrez l'ID de la tâche à marquer comme terminée: "))
                if todo_manager.MarquerTacheFinie(task_id):
                    print("Tâche marquée comme terminée!")
                else:
                    print("Erreur: ID de tâche invalide")
                    
            elif user_choice == "4":
                task_id = int(input("Entrez l'ID de la tâche à supprimer: "))
                if todo_manager.SupprimerTache(task_id):
                    print("Tâche supprimée!")
                else:
                    print("Erreur: ID de tâche invalide")
                    
            elif user_choice == "5":
                print("Au revoir!")
                logging.info("Application terminée normalement")
                break
                
            else:
                print("Choix invalide. Veuillez choisir entre 1-5")
                logging.warning(f"Choix de menu invalide: {user_choice}")
                
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
            logging.error("Entrée invalide reçue")

if __name__ == "__main__":
    main()
