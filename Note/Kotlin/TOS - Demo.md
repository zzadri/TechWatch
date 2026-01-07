
Step 1 : on va définir les dependances

```kotlin
plugins {
	// ...
}
android {
    // ...
}
dependencies {
    // Room Runtime et KTX (extensions coroutine)
    implementation("androidx.room:room-runtime:2.8.0")
    implementation("androidx.room:room-ktx:2.8.0")
    // Room Compiler (KSP ou KAPT) pour générer le code DAO/Database
    ksp("androidx.room:room-compiler:2.8.0")
}
```

Step 2 : dans data on va apres définir nos entité, une entité est une table de notre basse de donnée.

```kotlin
package com.monapp.home.data

import androidx.room.Entity
import androidx.room.PrimaryKey
import androidx.room.ColumnInfo

@Entity(tableName = "notes")
data class NoteEntity(
    @ColumnInfo(name = "title") val title: String,
    @ColumnInfo(name = "content") val content: String
) {
    @PrimaryKey(autoGenerate = true)
    var id: Long = 0L
}
```

Step 3 : ensuite toujours dans data on va créer nos DAO elle va permettre de CRUD nos donner dans notre base

```kotlin
package com.monapp.home.data

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query

@Dao
interface NoteDao {
    @Query("SELECT * FROM notes ORDER BY id DESC")
    fun getAllNotes(): kotlinx.coroutines.flow.Flow<List<NoteEntity>>

    @Insert
    suspend fun insertNote(note: NoteEntity)
}
```

Step 4 : mais des table sans bdd ça sert a rien donc on défini notre bdd c'est un sqlite

```kotlin
package com.monapp.home.data

import androidx.room.Database
import androidx.room.RoomDatabase

@Database(entities = [NoteEntity::class], version = 1, exportSchema = false)
abstract class NoteDatabase : RoomDatabase() {
    abstract fun noteDao(): NoteDao
}
```

Step 5 : ensuite on va définir un repos pour appeler nos donnes : 

le model :
```kotlin
package com.monapp.home.domain

data class Note(
	val id: Long = 0L, 
	val title: String, 
	val content: String
)
```

le repos :
```kotlin
package com.monapp.home.domain

import kotlinx.coroutines.flow.Flow

interface NoteRepository {
    fun getAllNotes(): Flow<List<Note>>
    suspend fun addNote(note: Note)
}

```

# vibreur

dans le manifest il faut définir au préalable ceci
```kotlin
<uses-permission android:name="android.permission.VIBRATE" />
```