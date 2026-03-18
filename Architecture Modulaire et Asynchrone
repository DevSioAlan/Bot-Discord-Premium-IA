# --- EXTRAIT : Initialisation Asynchrone & Chargement des Modules (Cogs) ---
class ProfessionalBot(commands.Bot):
    def __init__(self):
        # ... (Intents omis pour la clarté) ...
        super().__init__(command_prefix="s!", intents=intents, help_command=None)
        
        # Définition des modules séparés pour un code propre et maintenable
        self.initial_extensions = ['cogs.ai_concierge', 'cogs.leveling', 'cogs.reaction_roles']
        self.db = None

    async def setup_hook(self):
        # Connexion non-bloquante à la base de données
        self.db = await connect_db() 
        
        # Chargement dynamique des fonctionnalités
        for extension in self.initial_extensions:
            await self.load_extension(extension)
            
        # Synchronisation globale des commandes Slash
        await self.tree.sync()
