# Plugins

103,077 Claude Code plugins: every entry of every `.claude-plugin/marketplace.json` the crawl found, with what it does, where it lives and what is inside it.

## Get it

- [`plugins.csv`](plugins.csv) (36 MB)

Columns: `name`, `description`, `category`, `keywords`, `version`, `repo`, `url`, `stars`, `license`, `last_pushed`, `skills`, `commands`, `agents`, `hook_files`, `mcp_configs`, `marketplace_repo`, `marketplace_name`, `marketplaces`, `copies`, `repo_gone`.

## Notes

- Built from 122,249 marketplace entries. A plugin listed in several marketplaces appears once; copies with the same name and description under other repos (forks, mirrors) are folded into the original (`copies`).
- 90,349 have a description, in the author's words, cut at 600 characters. 2,534 of those were blank in the marketplace and filled from the plugin's own `plugin.json` or its repo description.
- `skills`, `commands`, `agents`, `hook_files`, `mcp_configs` count the files found under the plugin's folder.
- To install one: `/plugin marketplace add <marketplace_repo>` then `/plugin install <name>@<marketplace_name>`.
- 3,411 point at a repo that was already deleted or renamed at crawl time (`repo_gone`).
- `stars`, `license` and `last_pushed` belong to the repo, not the plugin.

## Browse

- [0-9-001](0-9-001.md): 374 entries, .NET Backend Patterns to 系统架构
- [a-001](a-001.md): 1,317 entries, a to agd-memory
- [a-002](a-002.md): 1,376 entries, Age Of Claude Soundpack to agentic
- [a-003](a-003.md): 1,344 entries, agentic to ai-readiness
- [a-004](a-004.md): 1,337 entries, ai-readiness-assessment to anatomiya
- [a-005](a-005.md): 1,283 entries, anatommy to apify-tech-stack-prospecting
- [a-006](a-006.md): 1,300 entries, apify-threads-search to ask-jev
- [a-007](a-007.md): 1,348 entries, ask-kiro to awesome-readme
- [a-008](a-008.md): 490 entries, awesome-readme to azzist
- [b-001](b-001.md): 1,364 entries, b to biome-vcs-integration
- [b-002](b-002.md): 1,381 entries, biomedical-ai to browser-mcp
- [b-003](b-003.md): 704 entries, browser-modes to byunk-claude-code-toolkit
- [c-001](c-001.md): 1,381 entries, c to ccfg-shell
- [c-002](c-002.md): 1,368 entries, ccfg-sqlite to clarity
- [c-003](c-003.md): 1,346 entries, clarity to claude-multi
- [c-004](c-004.md): 1,357 entries, claude-multi-agent-architecture to clippy
- [c-005](c-005.md): 1,369 entries, clippy to codebase-xray
- [c-006](c-006.md): 1,390 entries, codebasescout to company
- [c-007](c-007.md): 1,310 entries, company to continuous-monitor
- [c-008](c-008.md): 1,327 entries, continuuiti to creative
- [c-009](c-009.md): 1,095 entries, creative to czsc-chan-theory
- [d-001](d-001.md): 1,404 entries, d to debugging-tauri-apps
- [d-002](d-002.md): 1,317 entries, debugging-toolkit to design-stack
- [d-003](d-003.md): 1,330 entries, design-strategy to devTools
- [d-004](d-004.md): 1,295 entries, devtools to docs
- [d-005](d-005.md): 1,361 entries, docs to dutstech-ceoralph
- [d-006](d-006.md): 110 entries, duvo to dz0ny-devenv-claude
- [e-001](e-001.md): 1,299 entries, e-colleagues to engineering-multi-agent-systems-architect
- [e-002](e-002.md): 1,326 entries, engineering-multi-agent-systems-architect-zh to excel-foundry
- [e-003](e-003.md): 407 entries, excel-helper to ezsub
- [f-001](f-001.md): 1,313 entries, f-awesome-chatgpt-prompts-1 to finance-fpa-analyst
- [f-002](f-002.md): 1,421 entries, finance-fpa-analyst-zh to forgeplan
- [f-003](f-003.md): 1,154 entries, forgeplan-brownfield-pack to fzymgc-house-fzymgc-house-skills
- [g-001](g-001.md): 1,398 entries, g to git
- [g-002](g-002.md): 1,464 entries, git to gobbi
- [g-003](g-003.md): 1,361 entries, gobbler to GStack
- [g-004](g-004.md): 331 entries, gstack to gzp
- [h-001](h-001.md): 1,412 entries, h-mode to hinge-profile-optimizer
- [h-002](h-002.md): 1,274 entries, hinge-profile-optimizer to hyperfleet-architecture
- [h-003](h-003.md): 144 entries, hyperfleet-code-review to hzt
- [i-001](i-001.md): 1,285 entries, i to install-gnome-usage
- [i-002](i-002.md): 1,019 entries, install-guide-builder to izmailov
- [j-001](j-001.md): 1,402 entries, j-flow to jutsu-csharp
- [j-002](j-002.md): 144 entries, jutsu-cucumber to jyotish
- [k-001](k-001.md): 1,356 entries, k-dense-ai-claude-scientific-skills to kube-rbac
- [k-002](k-002.md): 133 entries, kube-recon to kyzo-python
- [l-001](l-001.md): 1,331 entries, l0st0-skills to libgdx-development
- [l-002](l-002.md): 1,355 entries, libkriging to Logtape Logging
- [l-003](l-003.md): 591 entries, logvalet to lz-advisor
- [m-001](m-001.md): 1,284 entries, m to markgrab
- [m-002](m-002.md): 1,409 entries, markie to memory-manager
- [m-003](m-003.md): 1,366 entries, memory-manager to mlo
- [m-004](m-004.md): 1,333 entries, mlops to mutation-testing
- [m-005](m-005.md): 296 entries, mutation-testing to mzizzi-ty-lsp
- [n-001](n-001.md): 1,296 entries, n to nlp-skills
- [n-002](n-002.md): 893 entries, nlp-text-analyzer to nzism-tanaji-hemant-naik
- [o-001](o-001.md): 1,407 entries, o-m-cc to openaccountants-mt
- [o-002](o-002.md): 1,313 entries, openaccountants-mx to otel-monitoring-setup
- [o-003](o-003.md): 263 entries, otel-ottl to ozma
- [p-001](p-001.md): 1,365 entries, p to perplexity-research
- [p-002](p-002.md): 1,374 entries, perplexity-search to Playwright Local
- [p-003](p-003.md): 1,413 entries, Playwright MCP to posit-dev-skills
- [p-004](p-004.md): 1,331 entries, position-manager-skill to process
- [p-005](p-005.md): 1,278 entries, process to proof-audit
- [p-006](p-006.md): 1,029 entries, proof-audit-2 to pyzotero
- [q-001](q-001.md): 798 entries, q to qyrusai-assure
- [r-001](r-001.md): 1,354 entries, r to redpanda-2
- [r-002](r-002.md): 1,343 entries, redpanda-connect to researcher
- [r-003](r-003.md): 1,341 entries, researcher to route-wise-screenshot-comparison-tool
- [r-004](r-004.md): 660 entries, routecraft-skills to rzpro
- [s-001](s-001.md): 1,252 entries, s to screenshotr
- [s-002](s-002.md): 1,310 entries, screenshotter to Senior Fullstack
- [s-003](s-003.md): 1,379 entries, Senior ML Engineer Templates to shipit
- [s-004](s-004.md): 1,358 entries, shipit-doc-system-bundle to skillforcer
- [s-005](s-005.md): 1,371 entries, skillforge to solo-sdlc
- [s-006](s-006.md): 1,335 entries, solo-selbststaendige-praxis to ssl-certificate-manager-5
- [s-007](s-007.md): 1,348 entries, ssl-certificate-manager-6 to suede-marketing
- [s-008](s-008.md): 1,370 entries, suede-skills to systematic-review
- [s-009](s-009.md): 41 entries, systemd to sztwiorok-buddy-plugin
- [t-001](t-001.md): 1,372 entries, t-view-automation to telnyx-webrtc
- [t-002](t-002.md): 1,359 entries, telnyx-whatsapp to ticketmill
- [t-003](t-003.md): 1,402 entries, tickets to transportrecht
- [t-004](t-004.md): 943 entries, trantor to Tzurot Deployment Guide
- [u-001](u-001.md): 1,301 entries, u to uzbekcha-spinner
- [v-001](v-001.md): 1,300 entries, v to visual-pr
- [v-002](v-002.md): 645 entries, visual-project-map to vz
- [w-001](w-001.md): 1,350 entries, W&B Plot Skill to wiki
- [w-002](w-002.md): 1,344 entries, wiki to writing
- [w-003](w-003.md): 263 entries, writing to wzkariampuzha-claude-skills
- [x-001](x-001.md): 576 entries, x to xyo-skills
- [y-001](y-001.md): 490 entries, y-context7 to yzmir-training-optimization
- [z-001](z-001.md): 524 entries, z to zzzprobe
