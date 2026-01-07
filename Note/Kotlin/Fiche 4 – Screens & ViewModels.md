## 1. Architecture UI et rôle des Screens

Un **Screen** représente une page complète de l’application.  
Chaque Screen est généralement divisé en plusieurs fonctions :

- **`@Composable Screen`** → fonction publique appelée dans le `NavHost`.
    
- **`Content`** → fonction privée contenant la logique UI (layout, éléments visuels).
    
- **`Preview`** → fonction privée pour visualiser l’écran dans Android Studio.
    

### Exemple de structure

```kotlin
@Composable
fun CharactersScreen(navController: NavController) {
    val viewModel: CharactersViewModel = viewModel()
    val state by viewModel.state.collectAsState()

    Content(
        state = state,
        onCharacterClick = { id -> navController.navigate("characterDetails/$id") }
    )
}

@Composable
private fun Content(
    state: CharactersState,
    onCharacterClick: (Int) -> Unit
) {
    LazyColumn {
        items(state.characters) { character ->
            CharacterCard(character, onClick = { onCharacterClick(character.id) })
        }
    }
}

@Preview(showBackground = true)
@Composable
private fun Preview() {
    Content(
        state = CharactersState(
            characters = listOf(
                Character(1, "Rick Sanchez", "rick.png"),
                Character(2, "Morty Smith", "morty.png")
            )
        ),
        onCharacterClick = {}
    )
}
```

---

## 2. Pourquoi utiliser des ViewModels ?

Les **ViewModels** répondent aux limites du cycle de vie des Activities/Fragments.

### Avantages :

- **Persistance des données** : survivent aux changements de configuration (rotation d’écran).
    
- **Gestion des états** : centralisation dans des `StateFlow` → prédictibilité.
    
- **Séparation des responsabilités** : UI ↔ logique métier.
    

---

## 3. Intégration ViewModel ↔ Screen

- Initialisé dans le Screen via `viewModel<MyViewModel>()`.
    
- Le **StateFlow** exposé est collecté avec `collectAsState()`.
    
- L’UI est **réactive** : se recompose automatiquement dès qu’un nouvel état est émis.
    

### Exemple de ViewModel

```kotlin
class CharactersViewModel(
    private val repository: CharactersRepository
) : ViewModel() {
    private val _state = MutableStateFlow(CharactersState())
    val state: StateFlow<CharactersState> = _state

    init {
        fetchCharacters()
    }

    private fun fetchCharacters() {
        viewModelScope.launch {
            val characters = repository.getAllCharacters()
            _state.value = CharactersState(characters = characters)
        }
    }
}
```

---

## 4. Clean Architecture et rôle des Repositories

- Les **Repositories** définissent les contrats de récupération des données.
    
- Organisation typique :
    
    - **Domain** → interfaces des repositories (contrats).
        
    - **Data** → implémentations concrètes (API, DB locale).
        
    - **Presentation** → Screens + ViewModels, qui ne connaissent que les interfaces.
        

💡 Cette structure garantit :

- Indépendance des couches.
    
- Facilité à tester (mock des repositories).
    
- Adaptabilité si la source de données change (API → DB locale).
    

---

## 5. Bonnes pratiques

- **Un seul point d’entrée public** par Screen (`Screen()`), tout le reste reste privé.
    
- **State immuable** (exposé via `val state: StateFlow`).
    
- **Preview systématique** → gain de temps en dev UI.
    
- Respecter la **séparation UI / logique** : ne jamais mettre de logique métier dans un Composable.
    

---

✅ **Résumé à retenir**

- Un **Screen** = page complète (structure : Screen, Content, Preview).
    
- Un **ViewModel** centralise les données et états, et survit au cycle de vie.
    
- `StateFlow` + `collectAsState()` = UI réactive et synchronisée.
    
- Clean Architecture → découplage grâce aux **repositories** et interfaces.