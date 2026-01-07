## 1. Composables et conception UI

- Un **composable** est une fonction annotée avec `@Composable` qui décrit une partie de l’UI.

- Les composables sont **déclaratifs** : on décrit _quoi afficher_ et Compose se charge du _comment_.

- Exemple d’un composable simple :

```kotlin
@Composable
fun CharacterCard(name: String, status: String) {
    Column(
        modifier = Modifier
            .padding(16.dp)
            .background(Color.LightGray)
    ) {
        Text(text = name, fontWeight = FontWeight.Bold)
        Text(text = "Status: $status")
    }
}
```

---

## 2. Exemple pratique : une Card personnalisée

- Objectif : représenter un **personnage** avec image + informations.

- Éléments importants :

    - `Image` → affichage d’une image depuis une URL (souvent avec **Coil**).

    - `Text` → contenu textuel.

    - `Modifier` → personnalisation (padding, taille, couleur, background, etc.).

    - `Spacer` → gérer les espacements.


```kotlin
@Composable
fun CharacterCard(character: Character) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(8.dp)
    ) {
        AsyncImage(                // Coil pour charger une image depuis une URL
            model = character.imageUrl,
            contentDescription = "${character.name} avatar",
            modifier = Modifier.size(80.dp)
        )
        Spacer(modifier = Modifier.width(16.dp))
        Column {
            Text(
                text = character.name,
                fontWeight = FontWeight.Bold
            )
            Text(
                text = "Status: ${character.status}",
                color = Color.Gray
            )
        }
    }
}
```

---

## 3. Architecture et Injection de dépendances

### Pourquoi une architecture claire ?

- Séparation des responsabilités.

- Facilite les tests, la maintenance et l’évolution.

- Compose s’intègre bien dans des architectures **Clean Architecture**.

![[Pasted image 20250911081935.png]]
### Koin – Injection de dépendances en Kotlin

- **Single** : une instance unique partagée.

- **Factory** : une nouvelle instance à chaque fois.

```kotlin
// Module de dépendances
val dataModule = module {
    single<ICharacterRepository> { CharacterRepository() } // instance unique
    factory { NetworkService() }                           // nouvelle instance
}

// Initialisation
startKoin {
    modules(dataModule)
}

// Utilisation dans une classe
class CharacterViewModel() : ViewModel() {
    private val repository: ICharacterRepository by inject()
}
```

💡 Métaphore du **sac et des ficelles** :

- Chaque objet est attaché à une ficelle avec une étiquette (le type).

- On tire la ficelle correspondant au type → on récupère l’objet.


---

## 4. Interfaces pour isoler les couches

- Une **interface** définit un contrat que d’autres couches implémentent.

- Permet de découpler **logique métier** et **implémentations concrètes**.

- Exemple typique en Clean Architecture :

    - `Domain` → définit l’interface du repository.

    - `Data` → fournit l’implémentation concrète (API, base locale).

    - `UI`/`Presentation` → consomme uniquement l’interface.


---

## 5. Responsiveness et bonnes pratiques UI

- Gestion de l’affichage **vertical / horizontal** selon la largeur de l’écran.

- Utilisation de `Row` ou `Column` dynamiquement.

- Ajustement du nombre de colonnes en **grille** en fonction de la largeur disponible.


```kotlin
// Exemple d’adaptation selon la largeur
val columns = (screenWidth / minCardWidth).coerceAtLeast(1)
LazyVerticalGrid(columns = GridCells.Fixed(columns)) {
    items(characters) { character ->
        CharacterCard(character)
    }
}
```

---

✅ **Résumé à retenir**

- Un **composable** = fonction déclarative qui construit un élément d’UI.

- **Koin** facilite la gestion des dépendances (Single vs Factory).

- Les **interfaces** garantissent la modularité et l’indépendance des couches.

- Adapter l’affichage aux tailles d’écran (responsive) = bonne pratique UI.
