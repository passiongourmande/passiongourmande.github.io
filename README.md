# Passion Gourmande by Lilya: website

Quarto website for Passion Gourmande (cake artist, Ottawa). Instagram: [@passion_gourmande_by_l](https://www.instagram.com/passion_gourmande_by_l/).
Three languages: English (root), French (`fr/`), Arabic right-to-left (`ar/`).

## Structure

| Path | What it is |
|---|---|
| `*.qmd` | English pages: `index`, `creations`, `gallery`, `order` |
| `fr/*.qmd`, `ar/*.qmd` | Same pages in French / Arabic. **Keep the same filenames**: the language switch maps `page.html` ↔ `fr/page.html` ↔ `ar/page.html`. |
| `tools/build_partials.py` | **Single source** for contact details, the Instagram posts shown, menu labels and the order form in all 3 languages. Generates `_partials/` |
| `_partials/` | Generated header, footer, order form, contact list, Instagram blocks (do not edit by hand) |
| `styles.scss` | Colours (cocoa `#3A2622`, blush `#F3DEDA`, rose `#9C4257`, gold `#C9A36A`), fonts, layout |
| `assets/logo-mark.svg`, `assets/cake.svg` | Logo mark and hero illustration |
| `assets/site.js` | Menu, language switch, two-step order form |
| `docs/` | Rendered website (what gets published) |

## Edit and preview

```bash
python tools/build_partials.py   # after changing contact details, Instagram posts, menu or form wording
quarto preview                    # live preview in the browser
quarto render                     # build the final site into docs/
```

Instagram embeds only load over http(s), not when opening the HTML file directly. Use `quarto preview`.

## Adding WhatsApp / email / phone

In `tools/build_partials.py`, fill `CO["whatsapp"]` (international digits, e.g. `16135551234`), `CO["email"]`
and/or `CO["phone"]`, then rebuild. The matching buttons (form "Send on WhatsApp" / "Send by email",
footer, contact list) appear automatically. While they are empty, the form sends via Instagram DM
(copy the prepared text → open the chat).

## Changing the Instagram posts

Edit `POSTS` in `tools/build_partials.py`: one `("p" or "reel", "<code>")` per post, where the code comes from
the post URL `instagram.com/p/<code>/`. The first `LATEST` (3) appear on the home page; all appear in the gallery.

## To confirm with Lilya before publishing

- [ ] City: Ottawa (inferred from Instagram)
- [ ] WhatsApp number, email, phone (currently Instagram only)
- [ ] Facebook link: `facebook.com/lilya.jas` is a personal profile; keep it or replace with a business page
- [ ] Product list: traditional sweets (*qalb el louz*), savoury bites, henna buffets, cheesecakes, 3D cakes
- [ ] "Meet Lilya" text and the quote attributed to her (written by us, she should approve or rewrite)
- [ ] Pickup / delivery policy, ordering lead time
- [ ] Which Instagram posts to feature
- [ ] Arabic and French wording: native review
- [ ] Optional: her own photos (would replace the illustration in the hero), her real logo if she has one

## Publish

`docs/` is a complete static site. GitHub Pages: push the repo, Settings → Pages → branch `main`, folder `/docs`.
A custom domain (e.g. `passiongourmande.ca`) can be attached later.
