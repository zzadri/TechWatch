## 1. Architecture des ressources

- Android distingue plusieurs types de **ressources** (couleurs, dimensions, chaînes, images, etc.).
    
- Trois grandes catégories de variables de couleur :
    
    - **Raw** → valeurs brutes (`#FFFFFF`, etc.).
        
    - **Business** → couleurs métier (ex. `primaryButton`, `errorText`).
        
    - **Material** → palette issue du `MaterialTheme`.
        

### Avantages

- Centralisation des valeurs → cohérence visuelle.
    
- Gestion automatique des **modes jour/nuit**.
    
- Support des **flavors** (par pays, marque, etc.).
    

---

## 2. Exemple : gestion des couleurs jour/nuit

### En XML (système Android natif)

**Jour :**

```xml
<resources>
    <color name="background">@color/iron</color>
    <color name="text">@color/mine_shaft</color>
</resources>
```

**Nuit :**

```xml
<resources>
    <color name="background">@color/shark</color>
    <color name="text">@color/wild_sand</color>
</resources>
```

➡️ Android choisit automatiquement la bonne palette.

---

### En Compose (gestion manuelle)

```kotlin
private val LightColors = lightColorScheme(
    primary = Color(0xFF98CBFF),
    background = Color(0xFFD9D9D9),
    onBackground = Color(0xFF333333),
    error = Color(0xFFD63D2E)
)

private val DarkColors = darkColorScheme(
    primary = Color(0xFF55CC44),
    background = Color(0xFF272B33),
    onBackground = Color(0xFFF5F5F5),
    error = Color(0xFFD63D2E)
)

@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colors = if (darkTheme) DarkColors else LightColors
    MaterialTheme(
        colorScheme = colors,
        content = content
    )
}
```

➡️ Plus flexible, mais nécessite de **gérer soi-même** les modes (et flavors).

---

## 3. Navigation dans Jetpack Compose

### Concepts principaux

- **NavHost** : conteneur de navigation, définit le graphe et la destination de départ.
    
- **NavGraph** : ensemble des destinations et relations entre elles.
    
- **NavController** : déclenche les actions de navigation (`navigate(...)`).
    

---

### Exemple basique

```kotlin
@Composable
fun AppNavHost(navController: NavController) {
    NavHost(
        navController = navController,
        startDestination = "home"
    ) {
        composable("home") { HomeScreen(navController) }
        composable(
            route = "details/{id}",
            arguments = listOf(navArgument("id") { type = NavType.IntType })
        ) { backStackEntry ->
            val id = backStackEntry.arguments?.getInt("id") ?: 0
            DetailsScreen(navController, id)
        }
    }
}
```

---

### Paramètres de navigation

- **Route dynamique** : `"details/{id}"` → accepte un paramètre.
    
- **Arguments** : définis avec un type (`IntType`, `StringType`, etc.).
    
- **BackStackEntry** : permet de récupérer les arguments passés.
    

➡️ Exemple d’appel :

```kotlin
navController.navigate("details/42")
```

→ ouvre l’écran `DetailsScreen` avec `id = 42`.

---

✅ **Résumé à retenir**

- Ressources : mieux vaut externaliser couleurs/chaînes pour centraliser.
    
- XML → gestion native des thèmes.
    
- Compose → plus souple mais gestion manuelle des palettes.
    
- Navigation Compose repose sur 3 éléments clés : **NavHost**, **NavGraph**, **NavController**.
    
- Routes dynamiques = passage d’arguments typés entre écrans.
