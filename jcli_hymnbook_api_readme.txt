hymnbook api 

Each file is an array  of song objects.

Song object properties

id (integer)
title (string)
language (string)
group (string)
tunelink (string)
verses (2D string array)
chorus(string array)
addedChorus(string array)

{
	"id": 1,
	"title": "Song title",
	"language": "English",
	"group": "Morning hymn",
	"tunelink":"https://www.ileewe.org/hymn1.mp3",
	"verses": [
				[
				"Verse 1, Line 1",
				"Verse 1, Line 2",
				"Verse 1, Line 3",
				"Verse 1, Line 4"
				],
				[
				"Verse 1, Line 1",
				"Verse 1, Line 2",
				"Verse 1, Line 3",
				"Verse 1, Line 4"
				]
			],
	"chorus": [
				"Chorus, Line 1",
				"Chorus, Line 2"
			],
	"addedChorus": [
						"Added chorus, Line 1",
						"Added chcorus, Line 2"
					]
}