# --- EXTRAIT : Système d'XP avec SQLite Asynchrone (aiosqlite) ---
async def update_user_xp(db: aiosqlite.Connection, user_id: int, xp_gain: int):
    current_data = await get_user_data(db, user_id)
    new_xp = current_data['xp'] + xp_gain
    current_level = current_data['level']
    required_xp = 50 * (current_level + 1)
    
    level_up = False
    if new_xp >= required_xp:
        new_level = current_level + 1
        new_xp -= required_xp
        level_up = True

    # Requête asynchrone optimisée avec ON CONFLICT
    await db.execute(
        "INSERT INTO users_xp (user_id, xp, level) VALUES (?, ?, ?) "
        "ON CONFLICT(user_id) DO UPDATE SET xp = excluded.xp, level = excluded.level", 
        (user_id, new_xp, new_level)
    )
    await db.commit()
    return level_up, new_level
