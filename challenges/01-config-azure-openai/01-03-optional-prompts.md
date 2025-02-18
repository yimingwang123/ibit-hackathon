# 01-03 Prompt Engineering Basics

In diesem Dokument findest du einige Übungen zum Üben von Prompt Engineering. Für jede Übung erhältst du einen Eingabetext und eine erwartete Vervollständigung. Deine Aufgabe besteht darin, den passenden Prompt zu schreiben, um die erwartete Vervollständigung zu erreichen.
___

## Übung 1 - Deutsche Übersetzung

* Aufgabe: Schreibe einen Prompt, der die erwartete Vervollständigung erzeugt.
* Eingabetext: `I was enjoying the sun, but then a huge cloud came and covered the sky.`
* Erwartete Vervollständigung: `Ich genoss die Sonne, aber dann kam eine riesige Wolke und bedeckte den Himmel.`

<details>
  <summary> Lösung anzeigen!</summary>

  ```
  Translate the following sentence into German.
    
  Sentence: I was enjoying the sun, but then a huge cloud came and covered the sky.
    
  German translation:
  ```
</details>

___

## Übung 2 - Negation

* Aufgabe: Schreibe einen Prompt, der die erwartete Vervollständigung erzeugt.
* Eingabetext: `I was enjoying the sun, but then a huge cloud came and covered the sky.`
* Erwartete Vervollständigung: `I was not enjoying the sun, and then a huge cloud did not come and cover the sky.`

<details>
  <summary> Lösung anzeigen!</summary>

  ```
  Negate the following sentence.
  Sentence: I was enjoying the sun, but then a huge cloud came and covered the sky.
  Negated sentence:
  ```
</details>

___

## Übung 3 - Klassifikation

* Aufgabe: Schreibe einen Prompt, der die erwartete Vervollständigung erzeugt.
* Eingabetext: `Not much to write about here, but it does exactly what it's supposed to. filters out the pop sounds. now my recordings are much more crisp. it is one of the lowest prices pop filters on amazon so might as well buy it, they honestly work the same despite their pricing.`
* Erwartete Vervollständigung (oder ähnlich):
  ``` 
  Positive: 0.75
  Neutral: 0.20
  Negative: 0.05
  ```

<details>
  <summary> Lösung anzeigen!</summary>

  ```
  Decide whether the product review's sentiment is positive, neutral or negative. Show the probability for positive, neutral and negative sentiment.
  ```
</details>

___

## Übung 4 - E-Mail-Zusammenfassung

* Aufgabe: Schreibe einen Prompt, der die erwartete Vervollständigung erzeugt.
* Eingabetext: Verwende deine eigene E-Mail...
* Erwartete Vervollständigung (oder ähnlich):
  ``` 
  Zusammenfassung: XYZ
  Offene Fragen: XYZ
  Handlungspunkte: XYZ 
  ```

<details>
  <summary> Lösung anzeigen!</summary>

  ```
  I want you to summarize the following email thread using this format:
  [Summary:]
  [Open Questions:]
  [Action Items:]
  ```
</details>

___

## Übung 5 - Umschreiben

* Aufgabe: Schreibe einen Prompt, der die erwartete Vervollständigung erzeugt.
* Eingabetext: `I was enjoying the sun, but then a huge cloud came and covered the sky.`
* Erwartete Vervollständigung: `She was enjoying the sun, but then a huge cloud came and covered the sky.`

<details>
  <summary> Lösung anzeigen!</summary>

  ```
  Convert the following sentence into third person singular, assuming the person is a female.
  Sentence: I was enjoying the sun, but then a huge cloud came and covered the sky.
  Converted sentence:
  ```
</details>

___

## Übung 6 - Mehrere Aufgaben

* Aufgabe: Schreibe einen Prompt, der die erwartete Vervollständigung erzeugt.
* Eingabetext: `I was enjoying the sun, but then a huge cloud came and covered the sky.`
* Erwartete Vervollständigung:
  ```
  {
      "translated": "Ich genoss die Sonne, aber dann kam eine riesige Wolke und bedeckte den Himmel.",
      "negated": "I was not enjoying the sun, and no huge cloud came and covered the sky.",
      "third_person": "She was enjoying the sun, but then a huge cloud came and covered the sky."
  }
  ```

<details>
  <summary> Lösung anzeigen!</summary>

  ```
  Take the following sentence and perform three tasks on it:
   
  1. Translate the sentence into German
  2. Negate the sentence
  3. Convert it into third person, and assume the person is a female.
  The output should be a JSON document. Use the keys "translated", "negated" and "third_person" in the JSON. No need to include the original text.
  Sentence: I was enjoying the sun, but then a huge cloud came and covered the sky.

  JSON:
  ```
</details>

___

___

##  Übung 7 - Datenextraktion nach JSON

* Übung: Schreibe eine Prompt, die die erwartete Completion generiert.
* Eingabetext:
```
Hallo, mein Name ist Mateo Gomez. Ich habe meine Kreditkarte am 17. August verloren und möchte ihre Sperrung beantragen. Der letzte Kauf, den ich getätigt habe, war ein Chicken Parmigiana Gericht im Contoso Restaurant, das sich in der Nähe des Hollywood Museums befindet, für 40 $. Nachfolgend meine persönlichen Informationen zur Validierung:
  Beruf: Buchhalter
  Sozialversicherungsnummer: 123-45-6789
  Geburtsdatum: 9-9-1989
  Telefonnummer: 949-555-0110
  Private Adresse: 1234 Hollywood Boulevard Los Angeles CA
  Verknüpfte E-Mail-Adresse: mateo@contosorestaurant.com
  Swift-Code: CHASUS33XXX
```
* Erwartete Completion:

```json
{
    "reason": "Lost card",
    "classified_reason": "lost_card",
    "name": "Mateo Gomez",
    "ssn": "123-45-6789",
    "dob": "09/09/1989"
}
```

<details>
  <summary>  Lösung anzeigen!</summary>
    ```
    Dies ist eine E-Mail von einem Kunden. Extrahiere die folgenden Informationen:
    - Grund der Kontaktaufnahme
    - Klassifizierter Grund der Kontaktaufnahme (kann einer der folgenden sein: "lost_card", "account_closure", "address_change")
    - Name des Kunden
    - Sozialversicherungsnummer
    - Geburtsdatum
    Extrahiere die Daten als JSON mit den Schlüsseln reason, classified_reason, name, ssn, dob. Für dob verwende das Format MM/DD/YYYY.
    ```

    E-Mail:
    Hallo, mein Name ist Mateo Gomez. Ich habe meine Kreditkarte am 17. August verloren und möchte ihre Sperrung beantragen. Der letzte Kauf, den ich getätigt habe, war ein Chicken Parmigiana Gericht im Contoso Restaurant, das sich in der Nähe des Hollywood Museums befindet, für 40 $. Nachfolgend meine persönlichen Informationen zur Validierung:
    Beruf: Buchhalter
    Sozialversicherungsnummer: 123-45-6789
    Geburtsdatum: 9-9-1989
    Telefonnummer: 949-555-0110
    Private Adresse: 1234 Hollywood Boulevard Los Angeles CA
    Verknüpfte E-Mail-Adresse: mateo@contosorestaurant.com
    Swift-Code: CHASUS33XXX

    Ergebnis:
    
</details>

___

##  Übung 8 - Mode-Produktbeschreibung
* Übung: Schreibe eine Prompt, die die erwartete Completion generiert
* Eingabetext:
  ```
  Saison: Winter
  Stil: Pullover
  Geschlecht: Weiblich
  Zielgruppe: Teenager
  Material: Baumwolle
  ```
* Erwartete Completion (oder ähnlich):
  ```
  Bleib diesen Winter warm und stylisch mit unseren gemütlichen Baumwollpullovern, perfekt für modebewusste Teenager. Erfrische deine Garderobe mit den neuesten Winterstyles aus unserer Kollektion.
  ```

<details>
  <summary> Lösung anzeigen!</summary>

  ```
  Schreibe eine zweisätzige Tagline für dieses Kleidungsstück. Mache sie ausführlicher.
  Saison: Winter
  Stil: Pullover
  Geschlecht: Weiblich
  Zielgruppe: Teenager
  Material: Baumwolle
  ```

</details>


___

##  Übung 9 - Schreibe einen Blogpost

* Übung: Schreibe einen Blogpost zu einem Thema deiner Wahl.
* Eingabetext: Du entscheidest.
* Erwartete Completion: Ein Blogpost mit Hashtags.

<details>
  <summary>  Lösung anzeigen!</summary>

Schritt 1: Überlege als Social Media Manager Blogpost-Ideen zu folgendem Thema: <Thema 1>.  
Schritt 2: Schreibe drei ansprechende und informative Absätze über <Idee 1 Beschreibung>.  
Schritt 3: Schreibe drei ansprechende und informative Absätze über <Idee 2 Beschreibung>.  
Schritt 4: Hashtags: <Liste relevanter #Hashtags>.  

</details>

___

##  Übung 10 - Callcenter

* Übung: Analysiere ein Callcenter-Gespräch.
* Eingabetext:

```
  Employee: "Hello, this is Julia Schreider from Contoso Company. How can I help you today?"
  Customer: "Hi, I am Carsten Mueller. I ordered a package 10 days ago, on February 10th, and it was supposed to arrive in maximum 5 business days. I have called three times already and nobody could provide any more information. I want to know where the package is and I want the problem to be solved immediately. This is the worst service I had for a long time!"
  Employee: "I apologize for the inconvenience, Mr. Mueller. I understand your frustration and I'm here to help. Can you please provide me with your order number so I can look into this for you?"
  Customer: "Yes, it's ACZ456789."
  Employee: "Thank you. I'm looking into it now. Can you please hold for a few minutes while I check the status of your package?"
  Customer: "Okay."
  Employee: "Thank you for your patience. I am sorry to inform you that I am unable to find the status of your package. It appears to have left the sending address, but no up-to-date status on the current location. I will further investigate your case and get back to you as soon as possible via phone call. Could you please provide me your contact information?"
  Customer: "Ah not again. Anyway, my phone number is +4911112223344."
  Employee: "I apologize again for the inconvenience. Is there anything else I can help you with today?"
  Customer: "No."
  Employee: "Thank you. Have a great day!"
  ```
* Erwartete Completion:

```json
{
    "classified_reason": "lost_package",
    "resolve_status": "unresolved",
    "call_summary": "Kunde hat Paket vor 10 Tagen bestellt und noch nicht erhalten.",
    "customer_name": "Carsten Mueller",
    "employee_name": "Julia Schreider",
    "order_number": "ACZ456789",
    "customer_contact_nr": "+4911112223344",
    "new_address": "N/A",
    "sentiment_initial": ["angry", "frustrated"],
    "sentiment_final": ["calm"],
    "satisfaction_score_initial": 0,
    "satisfaction_score_final": 5,
    "eta": "N/A",
    "action_item": ["track_package", "inquire_package_status", "contact_customer"]
}
```

<details>
  <summary> Lösung anzeigen!</summary>
  
  ```
  Below is a customer call transcription between customer call employee at Contoso Company and a customer. Extract the following information:

  - Classified reason for contact (can be one of "lost_package", "late_package", "address_change", "new_package_request")
  - Is the problem resolved? (can be one of "resolved", "unresolved")
  - Call summary (in max 100 characters)
  - Name of customer
  - Name of call center employee
  - Customer order number
  - Customer contact information (if not mentioned, then "N/A")
  - New customer address (if the call reason is to change address, else "N/A")
  - Customer's sentiment in the beginning of the call (can be one or more of "calm", "complaining", "angry", "frustrated", "unhappy", "neutral", "happy")
  - Customer's sentiment in the beginning of the call (can be one or more of "calm", "complaining", "angry", "frustrated", "unhappy", "neutral", "happy")
  - How satisfied is the customer in the beginning of the call, 0 being very unsatisfied and 10 being very satisfied
  - How satisfied is the customer in the end of the call, 0 being very unsatisfied and 10 being very satisfied
  - Estimated time of arrival of package
  - Action item (can be one or more of "no_action", "track_package", "inquire_package_status", "make_address_change", "cancel_order", "contact_customer)

  If customer is satisfied in the end, there is no follow up needed. Else, follow up with the relevant internal department to check the status.

  Extract it as JSON with keys classified_reason, resolve_status, call_summary, customer_name, employee_name, order_number, customer_contact_nr, new_address, sentiment_initial, sentiment_final, satisfaction_score_initial, satisfaction_score_final, eta, action_item.

  Employee: "Hello, this is Julia Schreider from Contoso Company. How can I help you today?"
  Customer: "Hi, I am Carsten Mueller. I ordered a package 10 days ago, on February 10th, and it was supposed to arrive in maximum 5 business days. I have called three times already and nobody could provide any more information. I want to know where the package is and I want the problem to be solved immediately. This is the worst service I had for a long time!"
  Employee: "I apologize for the inconvenience, Mr. Mueller. I understand your frustration and I'm here to help. Can you please provide me with your order number so I can look into this for you?"
  Customer: "Yes, it's ACZ456789."
  Employee: "Thank you. I'm looking into it now. Can you please hold for a few minutes while I check the status of your package?"
  Customer: "Okay."
  Employee: "Thank you for your patience. I am sorry to inform you that I am unable to find the status of your package. It appears to have left the sending address, but no up-to-date status on the current location. I will further investigate your case and get back to you as soon as possible via phone call. Could you please provide me your contact information?"
  Customer: "Ah not again. Anyway, my phone number is +4911112223344."
  Employee: "I apologize again for the inconvenience. Is there anything else I can help you with today?"
  Customer: "No."
  Employee: "Thank you. Have a great day!"

  JSON:
  ```

</details>


___

##  Übung 11 - Few-shot Learning

* Übung: Schreibe eine Few-shot Prompt, die eine Filmzusammenfassung klassifiziert.
* Beispieldaten:

```
  Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet's exclusive supply of the most precious resource in existence-a commodity capable of unlocking humanity's greatest potential-only those who can conquer their fear will survive.
  ['Action', 'Adventure', 'Science Fiction’]

  A botched store robbery places Wonder Woman in a global battle against a powerful and mysterious ancient force that puts her powers in jeopardy.
  ['Action', 'Adventure', 'Fantasy']

  After the devastating events of Avengers: Infinity War, the universe is in ruins due to the efforts of the Mad Titan, Thanos. With the help of remaining allies, the Avengers must assemble once more in order to undo Thanos' actions and restore order to the universe once and for all, no matter what consequences may be in store.
  ['Adventure', 'Science Fiction', 'Action']

  A widowed new dad copes with doubts, fears, heartache and dirty diapers as he sets out to raise his daughter on his own. Inspired by a true story.
  ['Drama', 'Family', 'Comedy’]

  New data:
  Harry, Ron and Hermione walk away from their last year at Hogwarts to find and destroy the remaining Horcruxes, putting an end to Voldemort's bid for immortality. But with Harry's beloved Dumbledore dead and Voldemort's unscrupulous Death Eaters on the loose, the world is more dangerous than ever.
``` 

* Erwartete Completion: Klassifizierung der neuen Daten.

<details>
  <summary> Lösung anzeigen!</summary>
  
  Add `###` as a stop sequence.

  ```
  You are adding tag categories to movies, based on their descriptions.

  ###
  Movie description: Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet's exclusive supply of the most precious resource in existence-a commodity capable of unlocking humanity's greatest potential-only those who can conquer their fear will survive.
  Tags: ['Action', 'Adventure', 'Science Fiction’]
  ###
  Movie description: A botched store robbery places Wonder Woman in a global battle against a powerful and mysterious ancient force that puts her powers in jeopardy.
  Tags: ['Action', 'Adventure', 'Fantasy']
  ###
  Movie description: After the devastating events of Avengers: Infinity War, the universe is in ruins due to the efforts of the Mad Titan, Thanos. With the help of remaining allies, the Avengers must assemble once more in order to undo Thanos' actions and restore order to the universe once and for all, no matter what consequences may be in store.
  Tags: ['Adventure', 'Science Fiction', 'Action']
  ###
  Movie description: A widowed new dad copes with doubts, fears, heartache and dirty diapers as he sets out to raise his daughter on his own. Inspired by a true story.
  Tags: ['Drama', 'Family', 'Comedy’]
  ###
  Movie description: Harry, Ron and Hermione walk away from their last year at Hogwarts to find and destroy the remaining Horcruxes, putting an end to Voldemort's bid for immortality. But with Harry's beloved Dumbledore dead and Voldemort's unscrupulous Death Eaters on the loose, the world is more dangerous than ever.
  Tags:
  ```

</details>

</details>

---
## Übung 12 - NL zu SQL mit Codex

* Aufgabe: Schreibe einen Prompt, der die erwartete SQL-Abfrage erzeugt.
* Tabelleninformationen:
  * Tabelle: customer // Spalten: firstname, name, customer_id, address
  * Tabelle: orders // Spalten: order_id, customer_id, product_id, product_amount
  * Tabelle: products // Spalten: product_id, price, name, description
* Erwartete Vervollständigung: Eine Abfrage, die die Top-10-Bestellungen zurückgibt und den Kundennamen anzeigt.

<details>
  <summary> Lösung anzeigen!</summary>

  ```
  """
  table customer, columns=firstname, name, customer_id, address
  table orders, columns=order_id, customer_id, product_id, product_amount
  table products, columns=product_id, price, name, description
  Write a query that returns the top 10 orders and show the customer name
  """

  query = 
  ```
</details>
