# Plugins

103,397 Claude Code plugins: every entry of every `.claude-plugin/marketplace.json` the crawl found, with what it does, where it lives and what is inside it.

## Get it

- [`plugins.csv`](plugins.csv) (37 MB)

Columns: `name`, `description`, `category`, `keywords`, `version`, `repo`, `url`, `stars`, `license`, `last_pushed`, `skills`, `commands`, `agents`, `hook_files`, `mcp_configs`, `marketplace_repo`, `marketplace_name`, `marketplaces`, `copies`, `repo_gone`.

## Notes

- Built from 123,568 marketplace entries. A plugin listed in several marketplaces appears once; copies with the same name and description under other repos (forks, mirrors) are folded into the original (`copies`).
- 91,280 have a description, in the author's words, cut at 600 characters. 2,677 of those were blank in the marketplace and filled from the plugin's own `plugin.json` or its repo description.
- `skills`, `commands`, `agents`, `hook_files`, `mcp_configs` count the files found under the plugin's folder.
- To install one: `/plugin marketplace add <marketplace_repo>` then `/plugin install <name>@<marketplace_name>`.
- 3,408 point at a repo that was already deleted or renamed at crawl time (`repo_gone`).
- `stars`, `license` and `last_pushed` belong to the repo, not the plugin.

## Browse

- [0-9-001](0-9-001.md): 374 entries, .NET Backend Patterns to 系统架构
- [a-001](a-001.md): 1,310 entries, a to ag2-agent-guide
- [a-002](a-002.md): 1,369 entries, ag2-agent-reviewer to agentforce-mobile-sdk
- [a-003](a-003.md): 1,331 entries, agentforce-mobile-sdk-android to ai-plugins-and-skills
- [a-004](a-004.md): 1,328 entries, ai-pm to analytics-qa
- [a-005](a-005.md): 1,306 entries, analytics-reporter to apify-logistics-and-delivery-routes
- [a-006](a-006.md): 1,257 entries, apify-market-monitor to ascii-explainer
- [a-007](a-007.md): 1,339 entries, ascii-graph-toolkit to avenor
- [a-008](a-008.md): 588 entries, aventerica89-bricks-builder-agent to azzist
- [b-001](b-001.md): 1,359 entries, b to Biome Linting
- [b-002](b-002.md): 1,379 entries, biome-claude-code-plugin to browser-extension-dev
- [b-003](b-003.md): 725 entries, browser-extension-engineering to byunk-claude-code-toolkit
- [c-001](c-001.md): 1,377 entries, c to ccfg-markdown
- [c-002](c-002.md): 1,362 entries, ccfg-mongodb to clari-pack-2
- [c-003](c-003.md): 1,333 entries, clarifai-skills to claude-memory
- [c-004](c-004.md): 1,353 entries, claude-memory to clio-coder-dev
- [c-005](c-005.md): 1,371 entries, clio-coder-test to codebase-onboarding
- [c-006](c-006.md): 1,386 entries, codebase-ops to compact-core
- [c-007](c-007.md): 1,306 entries, compact-core to context7-docs-fetcher
- [c-008](c-008.md): 1,323 entries, context7-docs-fetcher to create-qa-list
- [c-009](c-009.md): 1,160 entries, create-questions to czsc-chan-theory
- [d-001](d-001.md): 1,398 entries, d to debugging-discipline
- [d-002](d-002.md): 1,306 entries, debugging-doctrine-performance to design-review
- [d-003](d-003.md): 1,319 entries, design-review to devpowers
- [d-004](d-004.md): 1,282 entries, devproc to docker-outside-of-docker
- [d-005](d-005.md): 1,359 entries, docker-rocker to duckdb-skill
- [d-006](d-006.md): 173 entries, duckdb-skills to dz0ny-devenv-claude
- [e-001](e-001.md): 1,299 entries, e-colleagues to engineering-minimal-change-engineer
- [e-002](e-002.md): 1,313 entries, engineering-minimal-change-engineer-zh to excalidrawer
- [e-003](e-003.md): 431 entries, exceed-admin to ezsub
- [f-001](f-001.md): 1,310 entries, f-awesome-chatgpt-prompts-1 to finance-engineer-course
- [f-002](f-002.md): 1,414 entries, finance-financial-analyst to forgebee
- [f-003](f-003.md): 1,174 entries, forged to fzymgc-house-fzymgc-house-skills
- [g-001](g-001.md): 1,394 entries, g to git
- [g-002](g-002.md): 1,454 entries, git to goal-workflow-skills
- [g-003](g-003.md): 1,358 entries, goal2 to gs-superadmin
- [g-004](g-004.md): 372 entries, gsap to gzp
- [h-001](h-001.md): 1,406 entries, h-mode to hindsight
- [h-002](h-002.md): 1,272 entries, hindsight to hyper-cloaking
- [h-003](h-003.md): 159 entries, hyper-marketing to hzt
- [i-001](i-001.md): 1,278 entries, i to instacart-ads-toolkit
- [i-002](i-002.md): 1,037 entries, instacart-for-agents to izmailov
- [j-001](j-001.md): 1,392 entries, j-flow to jutsu-ansible
- [j-002](j-002.md): 158 entries, jutsu-apollo-graphql to jyotish
- [k-001](k-001.md): 1,324 entries, k-dense-ai-claude-scientific-skills to krzemienski-shannon-framework
- [k-002](k-002.md): 169 entries, krzysu-market-skills to kyzo-python
- [l-001](l-001.md): 1,318 entries, l0st0-skills to lhm-wordpress-hub
- [l-002](l-002.md): 1,346 entries, lhohan-agent-chisels to logmon-mcp
- [l-003](l-003.md): 625 entries, lognorth to lz-advisor
- [m-001](m-001.md): 1,280 entries, m to marketplace-validator
- [m-002](m-002.md): 1,401 entries, marketplace-validator to memory-hygiene
- [m-003](m-003.md): 1,357 entries, memory-hygiene to ml-skills
- [m-004](m-004.md): 1,317 entries, ml-superpowers to music-artist-os
- [m-005](m-005.md): 343 entries, music-catalog-diligence to mzizzi-ty-lsp
- [n-001](n-001.md): 1,292 entries, n to nixtla-vs-statsforecast-benchmark
- [n-002](n-002.md): 913 entries, nja to nzism-tanaji-hemant-naik
- [o-001](o-001.md): 1,400 entries, o to openaccountants-es
- [o-002](o-002.md): 1,310 entries, openaccountants-fi to otame4-research
- [o-003](o-003.md): 285 entries, otame4-sidework to ozma
- [p-001](p-001.md): 1,358 entries, p to perplexity
- [p-002](p-002.md): 1,373 entries, perplexity to playwright
- [p-003](p-003.md): 1,406 entries, playwright to portless
- [p-004](p-004.md): 1,331 entries, portless to problem
- [p-005](p-005.md): 1,269 entries, Problem Framing Canvas to prompting
- [p-006](p-006.md): 1,073 entries, prompting to pyzotero
- [q-001](q-001.md): 801 entries, q to qyrusai-assure
- [r-001](r-001.md): 1,351 entries, r to rednote-butler
- [r-002](r-002.md): 1,334 entries, rednote-mining to research-workflow
- [r-003](r-003.md): 1,338 entries, research-workflow to rosw
- [r-004](r-004.md): 691 entries, rot-dtd-commander to rzpro
- [s-001](s-001.md): 1,249 entries, s to screenshot-maker
- [s-002](s-002.md): 1,302 entries, screenshot-pr to send-to-kindle
- [s-003](s-003.md): 1,380 entries, sendgrid to ship-ready
- [s-004](s-004.md): 1,341 entries, ship-reviewed-prs to skill-vibe
- [s-005](s-005.md): 1,370 entries, skill-watch to soleon-observer
- [s-006](s-006.md): 1,315 entries, soleur to sr-harness
- [s-007](s-007.md): 1,346 entries, sr-harness to subimage-setup
- [s-008](s-008.md): 1,357 entries, subjective-label to syscode-agentic-skills
- [s-009](s-009.md): 126 entries, sysdesign to sztwiorok-buddy-plugin
- [t-001](t-001.md): 1,362 entries, t-view-automation to tellme-claude
- [t-002](t-002.md): 1,355 entries, tellonce to ticket-deflector
- [t-003](t-003.md): 1,397 entries, ticket-estimator to transition
- [t-004](t-004.md): 977 entries, transitions to Tzurot Deployment Guide
- [u-001](u-001.md): 1,305 entries, u to uzbekcha-spinner
- [v-001](v-001.md): 1,292 entries, v to visual-generator
- [v-002](v-002.md): 663 entries, visual-glass to vz
- [w-001](w-001.md): 1,344 entries, W&B Plot Skill to wiki
- [w-002](w-002.md): 1,341 entries, wiki to writers-helper
- [w-003](w-003.md): 282 entries, writers-room to wzkariampuzha-claude-skills
- [x-001](x-001.md): 577 entries, x to xyo-skills
- [y-001](y-001.md): 490 entries, y-context7 to yzmir-training-optimization
- [z-001](z-001.md): 527 entries, z to zzzprobe
