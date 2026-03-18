# 🤖 Bot Discord Premium IA - Assistant & Concierge Intelligent

> **Note :** Ce dépôt présente l'architecture logicielle d'un bot Discord de niveau "Premium". L'objectif de ce projet est de démontrer la maîtrise des environnements asynchrones en Python, la modularité du code via les `Cogs`, et l'intégration d'une Intelligence Artificielle au sein d'une communauté.

## 🚀 À propos du projet
Le **Bot Discord Premium IA** n'est pas un simple bot de commandes. C'est un véritable assistant communautaire conçu pour être fluide, scalable et hébergé 24/7. En utilisant des bibliothèques asynchrones comme `aiosqlite`, ce bot garantit qu'aucune requête en base de données ne viendra bloquer les interactions des autres utilisateurs, offrant une expérience utilisateur sans latence, même sur de gros serveurs.

---

## ✨ Fonctionnalités Clés

* 🧠 **Concierge IA Intégré :** Un système intelligent capable de répondre aux questions des utilisateurs de manière contextuelle.
* ⚡ **Architecture Asynchrone :** Utilisation complète d'`asyncio` et d'`aiosqlite` pour des performances optimales sans *thread blocking*.
* 🧩 **Design Modulaire (Cogs) :** Code divisé en modules indépendants (Leveling, Reaction Roles, IA) facilitant la maintenance et l'ajout de nouvelles fonctionnalités.
* ⭐ **Système de Leveling Persistant :** Algorithme de calcul d'expérience avec montée en niveau mathématique et sauvegarde en temps réel.
* 🌐 **Hosting 24/7 embarqué :** Intégration d'un serveur web léger (Flask) exécuté sur un thread séparé pour maintenir le bot en vie via des services de *Keep-Alive*.

---

## 💻 Code Highlights (Extraits Choisis)

### 1. Optimisation : Base de données Asynchrone (`aiosqlite`)
L'utilisation de SQLite classique bloque le processus principal de Python. Ici, l'utilisation d'`aiosqlite` permet au bot de continuer à traiter les messages pendant que la base de données se met à jour en arrière-plan.

```python
async def update_user_xp(db: aiosqlite.Connection, user_id: int, xp_gain: int):
    current_data = await get_user_data(db, user_id)
    new_xp = current_data['xp'] + xp_gain
    current_level = current_data['level']
    required_xp = 50 * (current_level + 1)
    
    # Vérification du passage de niveau
    level_up = False
    if new_xp >= required_xp:
        new_level = current_level + 1
        new_xp -= required_xp
        level_up = True

    # Requête asynchrone optimisée avec ON CONFLICT (Upsert)
    await db.execute(
        "INSERT INTO users_xp (user_id, xp, level) VALUES (?, ?, ?) "
        "ON CONFLICT(user_id) DO UPDATE SET xp = excluded.xp, level = excluded.level", 
        (user_id, new_xp, new_level)
    )
    await db.commit()
    return level_up, new_level
