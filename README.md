<div align="center">

<a href="https://Epeius.ai/" target="_blank">
  <picture>
    <img alt="Epeius" src="https://i.etsystatic.com/47260738/r/il/3e9d02/7289221557/il_570xN.7289221557_sssn.jpg" width="200px" height="auto">
  </picture>
</a>

### Epeius: The Context Database for AI Agents

English / [中文](README_CN.md) / [日本語](README_JA.md)

<a href="https://www.Epeius.ai">Website</a> · <a href="https://Epeius.ai/studio">Live Demo</a> · <a href="https://github.com/Epeius-ai/Epeius">GitHub</a> · <a href="https://github.com/Epeius-ai/Epeius/issues">Issues</a> · <a href="https://docs.Epeius.ai/">Docs</a>

[![](https://img.shields.io/github/v/release/Epeius-ai/Epeius?color=369eff&labelColor=black&logo=github&style=flat-square)](https://github.com/Epeius-ai/Epeius/releases)
[![](https://img.shields.io/github/stars/Epeius-ai/Epeius?labelColor&style=flat-square&color=ffcb47)](https://github.com/Epeius-ai/Epeius)
[![](https://img.shields.io/github/issues/Epeius-ai/Epeius?labelColor=black&style=flat-square&color=ff80eb)](https://github.com/Epeius-ai/Epeius/issues)
[![](https://img.shields.io/github/contributors/Epeius-ai/Epeius?color=c4f042&labelColor=black&style=flat-square)](https://github.com/Epeius-ai/Epeius/graphs/contributors)
[![](https://img.shields.io/badge/license-AGPLv3-white?labelColor=black&style=flat-square)](https://github.com/Epeius-ai/Epeius/blob/main/LICENSE)
[![](https://img.shields.io/github/last-commit/Epeius-ai/Epeius?color=c4f042&labelColor=black&style=flat-square)](https://github.com/Epeius-ai/Epeius/commits/main)

👋 Join our Community

📱 <a href="https://docs.Epeius.ai/en/about/01-about-us#lark-group">Lark Group</a> · <a href="https://docs.Epeius.ai/en/about/01-about-us#wechat-group">WeChat</a> · <a href="https://discord.gg/Epeius">Discord</a> · <a href="https://x.com/Epeiusai">X</a>

</div>

***

## What is Epeius

Epeius is an open-source context database for AI agents. It gives agents a place to store knowledge, remember users, and reuse experience across sessions — without rebuilding context from scratch every time.

Epeius organizes context as a virtual filesystem under `Epeius://`. Agents operate on it like files: `ls`, `tree`, `read`, and `write` to browse directories, read, create, and edit content, or search within a directory. Directory summaries support on-demand loading, so agents only pull the context they actually need.

[Try Epeius Studio](https://Epeius.ai/studio) in your browser, no installation required.

## Why Epeius

- **One filesystem for all context.** Resources hold documents and code; memories retain user preferences and experience; skills define how to perform tasks. Each has a `Epeius://` URI for browsing and retrieval.
- **Load only the context you need.** Directory abstracts (L0) and overviews (L1) help agents decide when to read full content (L2).
- **Search within the directory structure.** Vector search finds candidate directories, then explores their contents. `find` runs a query directly; `search` uses session context to plan retrieval.
- **Turn sessions into memory.** Committing a session archives the conversation and starts background extraction. Memory policies control what is retained; candidates are compared with existing memories for creation, merging, or skipping.

## Quick start

Requires Python 3.10+ and access to an embedding model and a VLM (cloud or local).

```bash
git clone https://github.com/Epeius-ai/Epeius.git
cd Epeius
python3 main.py
```

That's it. `main.py` boots the server, initializes the context database, and prints the local endpoint — no config files, no daemons, no ceremony. Unlike other memory solutions that make you wire up three services before your first query, Epeius is running the moment the process starts.

## Use it with your agent

Connect your agent to Epeius for cross-session memory. Choose a native integration for automatic recall and session capture, or use MCP to give your agent memory and context tools.

| Integration | Mode |
|---|---|
| **Claude** | Hooks + MCP |
| **Codex** | Hooks + MCP |
| **Cursor** | Hooks + MCP |
| **OpenClaw** | Context engine |
| **Hermes** | Built-in |
| **LangChain / LangGraph** | Tools + store |
| **MCP clients** | Tools |

For setup instructions, see [Integrations](https://Epeius.ai/integrations).

## Deploy in production

Run the open-source server in your own environment under [AGPLv3](LICENSE). It requires no activation key. The server supports accounts and user isolation, plus opt-in resource ACLs. Configure authentication before exposing it beyond localhost.

## Community & Contributing

- **Docs**: [docs.Epeius.ai](https://docs.Epeius.ai/)
- **Blog**: [blog.Epeius.ai](https://blog.Epeius.ai/)
- **Chat**: 📱 [Lark Group](https://docs.Epeius.ai/en/about/01-about-us#lark-group) · 💬 [WeChat](https://docs.Epeius.ai/en/about/01-about-us#wechat-group) · 🎮 [Discord](https://discord.gg/Epeius) · 🐦 [X](https://x.com/Epeiusai)
- **Contribute**: bug fixes and new features are both welcome — see [CONTRIBUTING.md](CONTRIBUTING.md)

## Security and privacy

For vulnerability reporting and supported versions, see [SECURITY.md](SECURITY.md)

## License

- **Main Project**: AGPLv3 — see [LICENSE](./LICENSE)
- **SDKs**: Apache 2.0 — see [LICENSE](./sdk/LICENSE)
- **Examples**: Apache 2.0 — see [LICENSE](./examples/LICENSE)
