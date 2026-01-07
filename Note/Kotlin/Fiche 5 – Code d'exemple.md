## 1. Composables de base

```kotlin
@Composable
fun Greeting(name: String) {
    Text(text = "Bonjour $name 👋")
}
```

```kotlin
@Composable
fun CharacterCard(name: String, status: String) {
    Column(modifier = Modifier.padding(16.dp)) {
        Text(text = name, fontWeight = FontWeight.Bold)
        Text(text = "Status: $status", color = Color.Gray)
    }
}
```

---

## 2. Layouts & Modifiers

```kotlin
Row(modifier = Modifier.fillMaxWidth()) { ... }
Column(modifier = Modifier.padding(8.dp)) { ... }
Spacer(modifier = Modifier.height(16.dp))
Box(modifier = Modifier.background(Color.Red).size(40.dp))
```

---

## 3. Images (Coil)

```kotlin
AsyncImage(
    model = character.imageUrl,
    contentDescription = "${character.name} avatar",
    modifier = Modifier.size(80.dp)
)
```

---

## 4. Thèmes (Jour/Nuit)

```kotlin
private val LightColors = lightColorScheme(
    primary = Color(0xFF98CBFF),
    background = Color(0xFFD9D9D9)
)

private val DarkColors = darkColorScheme(
    primary = Color(0xFF55CC44),
    background = Color(0xFF272B33)
)

@Composable
fun AppTheme(darkTheme: Boolean = isSystemInDarkTheme(), content: @Composable () -> Unit) {
    val colors = if (darkTheme) DarkColors else LightColors
    MaterialTheme(colorScheme = colors, content = content)
}
```

---

## 5. Navigation Compose

```kotlin
@Composable
fun AppNavHost(navController: NavController) {
    NavHost(navController, startDestination = "home") {
        composable("home") { HomeScreen(navController) }
        composable(
            "details/{id}",
            arguments = listOf(navArgument("id") { type = NavType.IntType })
        ) { backStackEntry ->
            val id = backStackEntry.arguments?.getInt("id") ?: 0
            DetailsScreen(navController, id)
        }
    }
}

// Appel navigation
navController.navigate("details/42")
```

---

## 6. ViewModel + StateFlow

```kotlin
class CharactersViewModel(private val repository: CharactersRepository) : ViewModel() {
    private val _state = MutableStateFlow(CharactersState())
    val state: StateFlow<CharactersState> = _state

    init { fetchCharacters() }

    private fun fetchCharacters() {
        viewModelScope.launch {
            val characters = repository.getAllCharacters()
            _state.value = CharactersState(characters = characters)
        }
    }
}
```

```kotlin
@Composable
fun CharactersScreen(navController: NavController) {
    val viewModel: CharactersViewModel = viewModel()
    val state by viewModel.state.collectAsState()

    LazyColumn {
        items(state.characters) { character ->
            CharacterCard(character, onClick = { navController.navigate("details/${character.id}") })
        }
    }
}
```

---

## 7. Injection de dépendances (Koin)

```kotlin
val dataModule = module {
    single<ICharacterRepository> { CharacterRepository() }
    factory { NetworkService() }
}

startKoin { modules(dataModule) }

class CharacterViewModel() : ViewModel() {
    private val repo: ICharacterRepository by inject()
}
```

---

✅ **Résumé express**

- `@Composable` = UI déclarative.
    
- `Modifier` → personnalisation (taille, padding, couleur).
    
- `AsyncImage` (Coil) pour charger les images.
    
- `MaterialTheme` gère couleurs et typographies.
    
- `NavHost + NavController` = navigation.
    
- `ViewModel + StateFlow` = état persistant et réactif.
    
- **Koin** = injection simple (Single vs Factory).
