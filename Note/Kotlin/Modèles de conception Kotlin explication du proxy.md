![[Pasted image 20250930111220.png]]

Le proxy est un wrapper pour un objet utilisé en arrière-plan. Cela signifie qu'il peut fournir une logique supplémentaire pour cet objet. Le proxy et l'objet implémentent tous deux la même interface. Il est principalement utilisé lorsqu'un contrôle d'accès supplémentaire est nécessaire.
### Implémentation

Créez l'interface Subject, qui sera utilisée par les clients.
Créez la classe RealSubject, qui implémente Subject et constitue l'implémentation par défaut.
Créez la classe Proxy, qui implémente Subject et contient une valeur RealSubject.
L'objet proxy et l'objet réel implémentent tous deux la même interface. Il est principalement utilisé avec les services.

![[Pasted image 20250930111318.png]]

Diagramme de classe Proxy

Qu'obtenons-nous ainsi ?
La gestion du cycle de vie de RealSubject sans polluer le code des clients.
Proxy peut fonctionner même si RealSubject n'est pas disponible ou renvoie une erreur.
Vous pouvez introduire plusieurs classes Proxy sans avoir à modifier quoi que ce soit, car le client ne sait pas s'il utilise Proxy ou RealSubject, ce qui est conforme au principe ouvert/fermé.
Extension des fonctionnalités de RealSubject. Par exemple, vous pouvez ajouter une mise en cache contrôlée pour ce RealSubject spécifique.

###### Exemple

Votre tâche consiste à créer une application de chat. Pour ce faire, vous disposez d'une API qui reçoit et envoie des messages. Cependant, le chat doit être sécurisé. Cela signifie que vous devrez encoder et décoder les messages.

Commençons par définir l'interface ChatService :

```kotlin
interface ChatService {  
   fun sendMessage(message: String)   
   fun getMessage(): String  
}
```

Maintenant, nous devons implémenter DefaultChatService :

```kotlin
class DefaultChatService : ChatService {  
   override fun sendMessage(message: String) {  
      // Send message  
   }  
  
   override fun getMessage(): String {  
      // Get message  
   }  
}
```

Enfin, pour ajouter une couche de sécurité supplémentaire, nous créons ChatServiceSecureProxy :

```kotlin
class ChatServiceSecureProxy(private val encoder: Encoder) : ChatService {  
  private val chatService: ChatService = DefaultChatService()  
  
  override fun sendMessage(message: String) {  
    chatService.sendMessage(encoder.encode(message))  
  }  
  
  override fun getMessage(): String {  
      val message = chatService.getMessage()  
      return encoder.decode(message)  
  }  
}
```

Désormais, l'encodage et le décodage sont encapsulés dans une classe spéciale. Si certains messages n'ont pas besoin d'être sécurisés, nous pouvons toujours utiliser DefaultChatService, car les deux implémentent ChatService .