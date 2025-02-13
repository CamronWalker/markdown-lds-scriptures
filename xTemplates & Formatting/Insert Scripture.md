<%_*
	const now = tp.date.now("YYYY-MM-DD");
	const modalForm = app.plugins.plugins.modalforms.api;
	const result = await modalForm.openForm('Insert Scripture');
		if (result.status === 'cancelled') {
			return; 
		}
async function getVerses(book, chapter, verse) {
    let verses = [];
    let verseParts = verse.split(',').map(v => v.trim());

    for (let part of verseParts) {
        if (part.includes('-')) {
            let [startVerse, endVerse] = part.split('-').map(Number);
            for (let i = startVerse; i <= endVerse; i++) {
                verses.push(`![[${book}#${i}]]`);
            }
        } else {
            verses.push(`![[${book}#${part}]]`);
        }
    }
    return verses.join(' ');
}

switch(result.asString('{{Book}}')) {
    case "Book of Mormon":
        var book = await result.asString('{{Book of Mormon}}') + " ";
        var chapter = await result.asString('{{BoM Chapter}}');
        var verse = await result.asString('{{BoM Verse}}');
        var combineRef = await getVerses(book + chapter, chapter, verse);
        break;
    case "Doctrine and Covenants":
        var book = "D&C ";
        var chapter = await result.asString('{{D&C Section}}');
        var verse = await result.asString('{{D&C Verse}}');
        var combineRef = await getVerses(book + chapter, chapter, verse);
        break;
    case "New Testament":
        var book = await result.asString('{{New Testament}}') + " ";
        var chapter = await result.asString('{{Bible Chapter}}');
        var verse = await result.asString('{{Bible Verse}}');
        var combineRef = await getVerses(book + chapter, chapter, verse);
        break;
    case "Old Testament":
        var book = await result.asString('{{Old Testament}}') + " ";
        var chapter = await result.asString('{{Bible Chapter}}');
        var verse = await result.asString('{{Bible Verse}}');
        var combineRef = await getVerses(book + chapter, chapter, verse);
        break;
    case "Pearl of Great Price":
        switch(result.asString('{{Pearl of Great Price}}')) {
            case "Moses":
                var book = "Moses ";
                var chapter = await result.asString('{{Moses Chapter}}');
                var verse = await result.asString('{{PoGP Verse}}');
                var combineRef = await getVerses(book + chapter, chapter, verse);
                break;
            case "Abraham":
                var book = "Abraham ";
                var chapter = await result.asString('{{Abraham Chapter}}');
                var verse = await result.asString('{{PoGP Verse}}');
                var combineRef = await getVerses(book + chapter, chapter, verse);
                break;
            default:
                var book = await result.asString('{{Pearl of Great Price}}');
                var verse = await result.asString('{{PoGP Verse}}');
                var combineRef = await getVerses(book, "", verse);
                break;
        }
        break;
}
	
_%>
>[!scripture] [[<% book %><% chapter %>|<% book %><% chapter %>:<% verse %>]]
><% combineRef %>