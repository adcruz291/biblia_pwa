// Cliente de bolls.life (sin API key). Traducción fija: RV1960.
const BASE = "https://bolls.life";
const TRANSLATION = "RV1960";
 
async function getJSON(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status} al consultar ${url}`);
  return res.json();
}
 
/** Capítulo completo -> [{ pk, verse, text }, ...] */
export async function getChapter(bookId, chapter) {
  const data = await getJSON(`${BASE}/get-text/${TRANSLATION}/${bookId}/${chapter}/`);
  if (!Array.isArray(data) || data.length === 0) throw new Error("Capítulo vacío o inexistente.");
  return data;
}
 
/** Reto ★★: versículo al azar -> { book, chapter, verse, text } */
export function getRandomVerse() {
  return getJSON(`${BASE}/get-random-verse/${TRANSLATION}/`);
}
 
/** Un versículo -> { pk, verse, text }  (la API puede devolver objeto o arreglo de 1) */
export async function getVerse(bookId, chapter, verse) {
  const data = await getJSON(`${BASE}/get-verse/${TRANSLATION}/${bookId}/${chapter}/${verse}/`);
  const v = Array.isArray(data) ? data[0] : data;
  if (!v || !v.text) throw new Error("Versículo no encontrado.");
  return v;
}