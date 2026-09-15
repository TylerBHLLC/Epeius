<div align="center">

<a href="https://mnemos.ai/" target="_blank">
  <picture>
    <img alt="Mnemos" src="https://raw.githubusercontent.com/mnemos-ai/mnemos/main/docs/images/logo.svg" width="200px" height="auto">
  </picture>
</a>

### Mnemos: The Context Database for AI Agents

English / [中文](README_CN.md) / [日本語](README_JA.md)

<a href="https://www.mnemos.ai">Website</a> · <a href="https://mnemos.ai/studio">Live Demo</a> · <a href="https://github.com/mnemos-ai/mnemos">GitHub</a> · <a href="https://github.com/mnemos-ai/mnemos/issues">Issues</a> · <a href="https://docs.mnemos.ai/">Docs</a>

[![](https://img.shields.io/github/v/release/mnemos-ai/mnemos?color=369eff&labelColor=black&logo=github&style=flat-square)](https://github.com/mnemos-ai/mnemos/releases)
[![](https://img.shields.io/github/stars/mnemos-ai/mnemos?labelColor&style=flat-square&color=ffcb47)](https://github.com/mnemos-ai/mnemos)
[![](https://img.shields.io/github/issues/mnemos-ai/mnemos?labelColor=black&style=flat-square&color=ff80eb)](https://github.com/mnemos-ai/mnemos/issues)
[![](https://img.shields.io/github/contributors/mnemos-ai/mnemos?color=c4f042&labelColor=black&style=flat-square)](https://github.com/mnemos-ai/mnemos/graphs/contributors)
[![](https://img.shields.io/badge/license-AGPLv3-white?labelColor=black&style=flat-square)](https://github.com/mnemos-ai/mnemos/blob/main/LICENSE)
[![](https://img.shields.io/github/last-commit/mnemos-ai/mnemos?color=c4f042&labelColor=black&style=flat-square)](https://github.com/mnemos-ai/mnemos/commits/main)

👋 Join our Community

📱 <a href="https://docs.mnemos.ai/en/about/01-about-us#lark-group">Lark Group</a> · <a href="https://docs.mnemos.ai/en/about/01-about-us#wechat-group">WeChat</a> · <a href="https://discord.gg/mnemos">Discord</a> · <a href="https://x.com/mnemosai">X</a>

</div>

***

## What is Mnemos

Mnemos is an open-source context database for AI agents. It gives agents a place to store knowledge, remember users, and reuse experience across sessions — without rebuilding context from scratch every time.

Mnemos organizes context as a virtual filesystem under `mnemos://`. Agents operate on it like files: `ls`, `tree`, `read`, and `write` to browse directories, read, create, and edit content, or search within a directory. Directory summaries support on-demand loading, so agents only pull the context they actually need.

[Try Mnemos Studio](https://mnemos.ai/studio) in your browser, no installation required.

## Why Mnemos

- **One filesystem for all context.** Resources hold documents and code; memories retain user preferences and experience; skills define how to perform tasks. Each has a `mnemos://` URI for browsing and retrieval.
- **Load only the context you need.** Directory abstracts (L0) and overviews (L1) help agents decide when to read full content (L2).
- **Search within the directory structure.** Vector search finds candidate directories, then explores their contents. `find` runs a query directly; `search` uses session context to plan retrieval.
- **Turn sessions into memory.** Committing a session archives the conversation and starts background extraction. Memory policies control what is retained; candidates are compared with existing memories for creation, merging, or skipping.

```
mnemos://
├── resources/              # Resources: project docs, repos, web pages, etc.
│   └── my_project/
│       ├── docs/
│       │   ├── api/
│       │   └── tutorials/
│       └── src/
└── user/
    └── {user_id}/
        ├── memories/
        │   └── preferences/
        │       ├── writing_style
        │       └── coding_habits
        ├── resources/
        │   └── private_project/
        ├── skills/
        │   ├── search_code
        │   └── analyze_data
        └── peers/
            └── web-visitor-alice/
```

The three loading tiers:

- **L0 (Abstract)**: a one-sentence summary for quick relevance checks.
- **L1 (Overview)**: core information and usage scenarios for planning.
- **L2 (Details)**: the full original data, read only when needed.

```
mnemos://resources/my_project/
├── .abstract.md           # L0: quick relevance check
├── .overview.md           # L1: structure and key points
└── docs/
    ├── .abstract.md
    ├── .overview.md
    └── api/
        ├── auth.md         # L2: full content, loaded on demand
        └── endpoints.md
```

## Quick start

Requires Python 3.10+ and access to an embedding model and a VLM (cloud or local).

```bash
git clone https://github.com/mnemos-ai/mnemos.git
cd mnemos
python3 main.py
```

That's it. `main.py` boots the server, initializes the context database, and prints the local endpoint — no config files, no daemons, no ceremony. Unlike other memory solutions that make you wire up three services before your first query, Mnemos is running the moment the process starts.

In another terminal, use the bundled `mn` CLI:

```bash
mn status
mn add-resource https://github.com/mnemos-ai/mnemos
mn ls mnemos://resources/
mn tree mnemos://resources/mnemos -L 2
mn find "what is Mnemos"
mn grep "Mnemos" --uri mnemos://resources/mnemos/docs/en
```

`mn find` returns matching context with URIs you can inspect. Build your own integration with the [Python](sdk/python/README.md), [Go](sdk/go/README.md), or [TypeScript](sdk/typescript/README.md) SDK, or the [HTTP API](https://docs.mnemos.ai/en/api/01-overview).

## Use it with your agent

Connect your agent to Mnemos for cross-session memory. Choose a native integration for automatic recall and session capture, or use MCP to give your agent memory and context tools.

| Integration | Mode |
|---|---|
| **Claude** | Hooks + MCP |
| **Codex** | Hooks + MCP |
| **Cursor** | Hooks + MCP |
| **OpenClaw** | Context engine |
| **Hermes** | Built-in |
| **LangChain / LangGraph** | Tools + store |
| **MCP clients** | Tools |

For setup instructions, see [Integrations](https://mnemos.ai/integrations).

## Deploy in production

Run the open-source server in your own environment under [AGPLv3](LICENSE). It requires no activation key. The server supports accounts and user isolation, plus opt-in resource ACLs. Configure authentication before exposing it beyond localhost.

## Community & Contributing

- **Docs**: [docs.mnemos.ai](https://docs.mnemos.ai/)
- **Blog**: [blog.mnemos.ai](https://blog.mnemos.ai/)
- **Chat**: 📱 [Lark Group](https://docs.mnemos.ai/en/about/01-about-us#lark-group) · 💬 [WeChat](https://docs.mnemos.ai/en/about/01-about-us#wechat-group) · 🎮 [Discord](https://discord.gg/mnemos) · 🐦 [X](https://x.com/mnemosai)
- **Contribute**: bug fixes and new features are both welcome — see [CONTRIBUTING.md](CONTRIBUTING.md)

## Security and privacy

For vulnerability reporting and supported versions, see [SECURITY.md](SECURITY.md)

## License

- **Main Project**: AGPLv3 — see [LICENSE](./LICENSE)
- **SDKs**: Apache 2.0 — see [LICENSE](./sdk/LICENSE)
- **Examples**: Apache 2.0 — see [LICENSE](./examples/LICENSE)
