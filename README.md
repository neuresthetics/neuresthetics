<h1 align="center">🧠 Neuresthetics</h1>

<p align="center">
  <b>Jason Burns</b> · 📍 Portland, OR · 🌐 <a href="https://neuresthetic.net">neuresthetic.net</a>
</p>

<p align="center">
  <a href="https://neuresthetic.net"><img src="https://img.shields.io/badge/neuresthetic.net-c9a227?style=for-the-badge&logo=googlechrome&logoColor=white" alt="neuresthetic.net"></a>
  <img src="https://img.shields.io/badge/builder-tools_%2B_research-2d2d2d?style=for-the-badge" alt="builder: tools and research">
  <img src="https://img.shields.io/badge/since-2017-3aa0ff?style=for-the-badge" alt="since 2017">
</p>

> **Neuresthetics** is *kinesthetics for brains*: spelled with "eu," never "neuroesthetics." Plural, it's the practice: shaping how a mind is organized, on purpose. Singular, a **neuresthetic** is a result of that practice.

I build tools for people who work with their hands and their heads: 🛠️ field kits for restoration techs, 🗣️ a word board for kids learning to talk, and 📜 long-running research on how minds put order on the world. Neuresthetics started before AI. AI is one of the tools now, not the point.

## ⚙️ HOW IT'S BUILT

**Local models.** A Linux tower with a 20 GB GPU and 64 GB RAM runs Ollama with Qwen 27B, in a standard and an uncensored build, at 16K context. A stock 14B is being added for model-swap runs. The tower works through unattended job queues, for days if needed, for an adversarial argument harness: the models draft the strongest case for each side, code checks every cite against word-for-word source excerpts, and runs are rescored and repeated across seeds and model swaps to see how much of a result comes from the model.

**Grok.** Grok Bot (an xAI assistant) runs a set of project bots for coding, audits, writing support, and fetching the word-for-word sources those cite checks use.

## 🛠️ "REAL WORLD" PRODUCTS

<sub>Made to be useful to other people.</sub>

<table>
  <tr>
    <td><a href="https://neuresthetics.github.io/restokit/"><img src="img/wide-restokit-brand.jpg" width="100%" alt="The RestoKit logo, a sand house with a copper drying curve, on deep teal over a faint drying log"></a></td>
  </tr>
  <tr>
    <td>
      <h3>💧 <a href="https://neuresthetics.github.io/restokit/">RestoKit</a></h3>
      A restoration kit for water, mold, and crawlspace jobs, built for any level from tech to PM and estimator. Grounded in IICRC S500 and S520, it walks a job in order and holds the rare edge cases.<br><br>
      <sub>⚙️ <b>Runs on:</b> Commercial cloud models · loaded into the Grok app or a Grok Bot</sub><br>
      🌐 <a href="https://neuresthetics.github.io/restokit/">page</a> · 📂 <a href="https://github.com/neuresthetics/resto_kit_public">repo</a>
    </td>
  </tr>
</table>

<br>

<table>
  <tr>
    <td><a href="https://neuresthetics.github.io/anova/"><img src="img/wide-anova-hands.jpg" width="100%" alt="A child's hands holding a tablet running the ANOVA Language word board, with I want water in the message bar"></a></td>
  </tr>
  <tr>
    <td>
      <h3>🗣️ <a href="https://neuresthetics.github.io/anova/">ANOVA Language</a></h3>
      A free, offline AAC word board for iPad and other tablets. Buttons stay put as word levels grow. MIT licensed.<br><br>
      <sub>⚙️ <b>Runs on:</b> No model · plain HTML, CSS and JavaScript, offline, no network calls</sub><br>
      🌐 <a href="https://neuresthetics.github.io/anova/">page</a> · 📂 <a href="https://github.com/neuresthetics/anova_language_dev_public">repo</a>
    </td>
  </tr>
</table>

<br>

<table>
  <tr>
    <td><a href="https://neuresthetics.github.io/grokipedia/"><img src="img/wide-grokipedia.jpg" width="100%" alt="Grokipedia Truth Audit"></a></td>
  </tr>
  <tr>
    <td>
      <h3>🔎 <a href="https://neuresthetics.github.io/grokipedia/">Grokipedia Truth Audit</a></h3>
      Reproducible audits of Grokipedia articles on saved snapshots: fallacy scans and citation checks, with the data and scripts to check them. So far: 58 circumcision-related articles and the Spinoza article.<br><br>
      <sub>⚙️ <b>Runs on:</b> Grok · a model reads saved snapshots against the substance_lens fallacy catalogue; scripts verify quotes and citations</sub><br>
      🌐 <a href="https://neuresthetics.github.io/grokipedia/">page</a> · 📂 <a href="https://github.com/neuresthetics/grokipedia-truth-audit">repo</a>
    </td>
  </tr>
</table>

<br>

<table>
  <tr>
    <td><a href="https://neuresthetics.github.io/substance-lens/"><img src="img/wide-substance-lens.jpg" width="100%" alt="A lens over an argument graph: surviving steps glow gold, cut steps are struck out with fallacy codes"></a></td>
  </tr>
  <tr>
    <td>
      <h3>🔍 <a href="https://neuresthetics.github.io/substance-lens/">substance_lens</a></h3>
      A JSON prompt spec: paste it into a chat model, give it a claim, and it checks the argument step by step and scans both the claim and its strongest counter-case for 67 fallacies. Flags are judgments to verify, not proofs.<br><br>
      <sub>⚙️ <b>Runs on:</b> Any capable chat model · a prompt spec, built with Grok in mind; no code ships</sub><br>
      🌐 <a href="https://neuresthetics.github.io/substance-lens/">page</a> · 📂 <a href="https://github.com/neuresthetics/substance_lens">repo</a>
    </td>
  </tr>
</table>

<br>

## 🧠 BRAND PROJECT

<sub>The Neuresthetics project itself: one inquiry, in three parts.</sub>

The study, the book and split_load_sim are the three sides of the Neuresthetics project. The Genius Study (v8) collects sourced records of remembered geniuses and states a labeled belief model about how early lawful form might pay off; the book builds, axiom by axiom, the one order (God or Nature) to which the brain and its society belong. split_load_sim is how we go between them. None of the three comes first; each draws on the other two, circling one goal. split_load_sim grows graphs as models of how a mind's maps could be structured, drawing on the book's axioms and testing whether the study's Lane B assumptions produce the effect they claim inside the model. Its results are model outputs, not findings, and the study has no results yet. The book in turn tries to key in on what makes v8 go around, and findings in any one can send the others back to work.

<p align="center">
  <img src="img/side-projects-map.png" width="720" alt="Map of the side projects: an equilateral triangle with the Neuresthetics Genius Study (v8, no results yet), split_load_sim (graph-growth models, model outputs, not findings) and Freedom of Necessity (the book) at the corners, each joined to the other two and to a circle at the centre that reads 'one goal: the order of the mind'">
</p>

<table>
  <tr>
    <td><a href="https://neuresthetics.github.io/study/"><img src="img/short-study-faces.jpg" width="100%" alt="Portraits of people from the study's roster fading into a crowd of about 1,380"></a></td>
  </tr>
  <tr>
    <td>
      <b>🔬 <a href="https://neuresthetics.github.io/study/">Neuresthetics Genius Study</a></b><br>
      <b>The study.</b> Where remembered genius sits on a scale of lawful, non-intervening order, with a labeled belief model. v8 is in progress; no results yet.<br>
      <sub>⚙️ <b>Runs on:</b> Grok · Grok Bot agents draft person records from web search and the cited pages (unreviewed)</sub><br>
      <sub>🌐 <a href="https://neuresthetics.github.io/study/">page</a> · 📂 <a href="https://github.com/neuresthetics/neuresthetics_genius_study">repo</a> · 🖼️ <a href="img/study-faces-credits.md">portrait credits</a></sub>
    </td>
  </tr>
  <tr>
    <td><a href="https://neuresthetics.github.io/book/"><img src="img/short-book-graph.jpg" width="100%" alt="The book's dependency graph (12 items, 33 links) drawn over a page of Spinoza's 1677 Ethics"></a></td>
  </tr>
  <tr>
    <td>
      <b>📖 <a href="https://neuresthetics.github.io/book/">Freedom of Necessity</a></b><br>
      <b>The book.</b> A Spinoza-style geometric book on one order, God or Nature, to which the brain and its society belong.<br>
      <sub>⚙️ <b>Runs on:</b> Local Qwen 27B · checks each entry against what it cites; argument harness in progress</sub><br>
      <sub>🌐 <a href="https://neuresthetics.github.io/book/">page</a> · 📂 <a href="https://github.com/neuresthetics/freedom_of_necessity">repo</a> · 🖼️ <a href="img/book-credits.md">image credit</a></sub>
    </td>
  </tr>
  <tr>
    <td><a href="https://neuresthetics.github.io/split-load-sim/"><img src="img/short-split-load-sim.jpg" width="100%" alt="An exception_prior run from split_load_sim: a teal main map joined to an amber reserved map by one bottleneck edge"></a></td>
  </tr>
  <tr>
    <td>
      <b>🧬 <a href="https://neuresthetics.github.io/split-load-sim/">split_load_sim</a></b><br>
      <b>The bridge.</b> Graph-growth models that connect the study and the book, descended from <a href="https://github.com/neuresthetics/graphtacular">graphtacular</a> (2019). Model outputs, not findings.<br>
      <sub>⚙️ <b>Runs on:</b> No model · seeded Python graph models</sub><br>
      <sub>🌐 <a href="https://neuresthetics.github.io/split-load-sim/">page</a> · 📂 <a href="https://github.com/neuresthetics/split_load_sim">repo</a></sub>
    </td>
  </tr>
</table>
