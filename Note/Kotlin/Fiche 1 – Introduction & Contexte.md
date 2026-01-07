## 1. Kotlin et Jetpack Compose

- **Kotlin** : langage officiel recommandé par Google pour Android.
    
    - Syntaxe moderne, concise et sûre (null-safety).

    - Compatible avec tout l’écosystème Java.

- **Jetpack Compose** :
    
    - Toolkit moderne pour construire des UI déclaratives.

    - Remplace les layouts XML classiques.

    - Basé sur des **Composables** (fonctions annotées avec `@Composable`).


---

## 2. Développement orienté composant

- Chaque élément de l’UI est un **composable réutilisable**.
    
- Avantages :
    
    - **Lisibilité** : chaque partie de l’écran est isolée.
        
    - **Réutilisation** : les composants sont modulaires.
        
    - **Évolutivité** : plus facile à maintenir et à tester.
        

### Exemple simple :

```kotlin
@Composable
fun Greeting(name: String) {
    Text(text = "Bonjour $name 👋")
}
```

---

## 3. Genèse d’Android (rappel rapide)

- Android a évolué d’un système basé sur XML vers une approche **plus réactive et déclarative**.
    
- Pourquoi Compose ?
    
    - Limiter la lourdeur du XML.
        
    - Simplifier la gestion des états et du cycle de vie.
        
    - Faciliter l’adaptation aux écrans variés.
        

---

## 4. Le rôle du **Context**

- Fournit des informations globales sur l’environnement de l’application.
    
- Sert à accéder :
    
    - aux ressources (`getString(R.string.nom)`),
        
    - aux services système (ex. `ConnectivityManager`),
        
    - à la gestion des fichiers et préférences.
        
- ⚠️ Important en Compose : certains composants (images, caches, etc.) nécessitent encore un `Context`.
    

---

## 5. Mise en place de l’environnement

- Initialisation d’un **projet Sandbox** pour expérimenter.
    
- Configuration de l’**émulateur Android** personnalisé.
    
- Vérification que tous les outils (Android Studio, SDK, émulateur) fonctionnent.
    
- Objectif : disposer d’un cadre de test stable pour se concentrer sur l’apprentissage.
    

---

✅ **Résumé à retenir**

- Kotlin + Compose = combo moderne recommandé pour Android.
    
- Approche déclarative → chaque UI est une fonction `@Composable`.
    
- Le **Context** reste une notion clé pour interagir avec l’environnement Android.
    
- Projet d’essai (sandbox) utile uniquement comme terrain d’expérimentation.