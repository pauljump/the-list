# Plugins

112,929 Claude Code plugins: every entry of every `.claude-plugin/marketplace.json` the crawl found, with what it does, where it lives and what is inside it.

## Get it

- [`plugins.csv`](plugins.csv) (40 MB)

Columns: `name`, `description`, `category`, `keywords`, `version`, `repo`, `url`, `stars`, `license`, `last_pushed`, `skills`, `commands`, `agents`, `hook_files`, `mcp_configs`, `marketplace_repo`, `marketplace_name`, `marketplaces`, `copies`, `repo_gone`.

## Notes

- Built from 135,266 marketplace entries. A plugin listed in several marketplaces appears once; copies with the same name and description under other repos (forks, mirrors) are folded into the original (`copies`).
- 101,094 have a description, in the author's words, cut at 600 characters. 3,176 of those were blank in the marketplace and filled from the plugin's own `plugin.json` or its repo description.
- `skills`, `commands`, `agents`, `hook_files`, `mcp_configs` count the files found under the plugin's folder.
- To install one: `/plugin marketplace add <marketplace_repo>` then `/plugin install <name>@<marketplace_name>`.
- 3,473 point at a repo that was already deleted or renamed at crawl time (`repo_gone`).
- `stars`, `license` and `last_pushed` belong to the repo, not the plugin.

## Browse

- [0-9-001](0-9-001.md): 407 entries, .NET Backend Patterns to 通用技能
- [a-001](a-001.md): 1,326 entries, a to aesthetic
- [a-002](a-002.md): 1,316 entries, aesthetic-foundations to agent-team-generic
- [a-003](a-003.md): 1,313 entries, agent-team-generic-copilot to ai-cmo
- [a-004](a-004.md): 1,311 entries, ai-coach to algo-trading-backtesting-methodology
- [a-005](a-005.md): 1,281 entries, algo-trading-broker-integration to anxiety
- [a-006](a-006.md): 1,277 entries, Any LLM as Tool to arcads
- [a-007](a-007.md): 1,301 entries, arcana to atom
- [a-008](a-008.md): 1,313 entries, atomgun to Axiom xOS Code Skills
- [a-009](a-009.md): 249 entries, axiom-audit-pipelines to azzist
- [b-001](b-001.md): 1,338 entries, b to bigslick-content
- [b-002](b-002.md): 1,336 entries, bigslick-gtm to brand-management
- [b-003](b-003.md): 1,132 entries, brand-md to byunk-claude-code-toolkit
- [c-001](c-001.md): 1,378 entries, c to cc0-audio
- [c-002](c-002.md): 1,359 entries, cc10x to cicd-automation-2
- [c-003](c-003.md): 1,300 entries, cicd-automation-3 to claude-ecosystem-promoter
- [c-004](c-004.md): 1,319 entries, claude-education-skills-library to claudeknows
- [c-005](c-005.md): 1,355 entries, claudelance-worker to Code Review Standards
- [c-006](c-006.md): 1,359 entries, Code Runner MCP Server to coding-agent-skills
- [c-007](c-007.md): 1,317 entries, coding-agent-skills to concept-rotation-monitor
- [c-008](c-008.md): 1,315 entries, concept-sketching to Copilot SDK Integration
- [c-009](c-009.md): 1,297 entries, Copilot Skills Suggester to crewai
- [c-010](c-010.md): 1,060 entries, CrewAI Multi-Agent Templates to czsc-chan-theory
- [d-001](d-001.md): 1,358 entries, d to DDIA Systems
- [d-002](d-002.md): 1,318 entries, ddia-engineering to design
- [d-003](d-003.md): 1,274 entries, design to developer-environment
- [d-004](d-004.md): 1,278 entries, developer-essentials to dispatch
- [d-005](d-005.md): 1,332 entries, dispatch to dotnet
- [d-006](d-006.md): 861 entries, dotnet to dz0ny-devenv-claude
- [e-001](e-001.md): 1,309 entries, e-colleagues to engineering-data-engineer-zh
- [e-002](e-002.md): 1,254 entries, engineering-data-visualization-engineer to everything-claude-code
- [e-003](e-003.md): 749 entries, everything-claude-code to ezsub
- [f-001](f-001.md): 1,309 entries, f-awesome-chatgpt-prompts-1 to File Test Bug Analyzer
- [f-002](f-002.md): 1,386 entries, file-and-image-utilities to focus-ai-brand
- [f-003](f-003.md): 1,330 entries, focus-attention-design to full-stack-dev-skills
- [f-004](f-004.md): 258 entries, full-stack-developer to fzymgc-house-fzymgc-house-skills
- [g-001](g-001.md): 1,391 entries, g to ghostie
- [g-002](g-002.md): 1,412 entries, ghostlight to glyph
- [g-003](g-003.md): 1,370 entries, glyph to green-code
- [g-004](g-004.md): 867 entries, green-gate-never-examined-the-case to gzp
- [h-001](h-001.md): 1,393 entries, h-level-docs to hex-grid
- [h-002](h-002.md): 1,236 entries, hex-pack to hugo
- [h-003](h-003.md): 500 entries, hugo to hzt
- [i-001](i-001.md): 1,269 entries, i to inkypal
- [i-002](i-002.md): 1,266 entries, inlab-human to izmailov
- [j-001](j-001.md): 1,366 entries, j-flow to juan-workflow
- [j-002](j-002.md): 321 entries, juanlurg-data-science-claude-skills-experiment-tr… to jz-tanstack-ship
- [k-001](k-001.md): 1,307 entries, k-dense-ai-claude-scientific-skills to Kotlin Spring Boot Starter
- [k-002](k-002.md): 320 entries, Kotlin Testing Suite to kyzo-python
- [l-001](l-001.md): 1,304 entries, l-lawliet to lesson-generator
- [l-002](l-002.md): 1,334 entries, lesson-learned to loanark-buyer-explainers
- [l-003](l-003.md): 945 entries, loanark-client-updates to lz-advisor
- [m-001](m-001.md): 1,274 entries, m to marketing-suite
- [m-002](m-002.md): 1,379 entries, marketing-suites to mem-forever
- [m-003](m-003.md): 1,332 entries, mem-forever to minesweeper
- [m-004](m-004.md): 1,330 entries, Minesweeper Game to motion-framer
- [m-005](m-005.md): 856 entries, motion-graphics-music-video to mzizzi-ty-lsp
- [n-001](n-001.md): 1,278 entries, n to niko-email
- [n-002](n-002.md): 1,106 entries, niko-engineering to nzism-tanaji-hemant-naik
- [o-001](o-001.md): 1,392 entries, o to OPC Skills
- [o-002](o-002.md): 1,304 entries, opc-develop to organizing-for-speed
- [o-003](o-003.md): 550 entries, organoid-biologist to ozma
- [p-001](p-001.md): 1,322 entries, p to perceptron
- [p-002](p-002.md): 1,371 entries, perchling to plank
- [p-003](p-003.md): 1,373 entries, plankeeper to pocketflow
- [p-004](p-004.md): 1,334 entries, PocketFlow Marketplace to pre-deploy-checklist
- [p-005](p-005.md): 1,259 entries, Pre-Earnings Preparation Report to project-board
- [p-006](p-006.md): 1,258 entries, project-bootstrap to PubMed Research Data
- [p-007](p-007.md): 592 entries, PubMed Search to pyzotero
- [q-001](q-001.md): 860 entries, q to qyrusai-assure
- [r-001](r-001.md): 1,324 entries, r to recruit
- [r-002](r-002.md): 1,324 entries, recruit to research
- [r-003](r-003.md): 1,309 entries, research to risk-sizing-not-blocking
- [r-004](r-004.md): 1,237 entries, riskmodels to rzpro
- [s-001](s-001.md): 1,213 entries, s to scite
- [s-002](s-002.md): 1,288 entries, scival to security-toolkit
- [s-003](s-003.md): 1,327 entries, security-toolkit to seyfert
- [s-004](s-004.md): 1,356 entries, sf to siyuan
- [s-005](s-005.md): 1,388 entries, siyuan to slim-changelog
- [s-006](s-006.md): 1,266 entries, slim-cli to speak
- [s-007](s-007.md): 1,358 entries, speak to starter-plugin
- [s-008](s-008.md): 1,284 entries, starter-session-audit to suno-prompt-architect
- [s-009](s-009.md): 1,348 entries, suno-song to system-memory-cleanup
- [s-010](s-010.md): 83 entries, system-overview-agents to sztwiorok-buddy-plugin
- [t-001](t-001.md): 1,336 entries, t-view-automation to techstack
- [t-002](t-002.md): 1,337 entries, techstack-identification to thinking-journey-map
- [t-003](t-003.md): 1,402 entries, thinking-kanban to torchdrug
- [t-004](t-004.md): 1,330 entries, torchshapeflow to TypeORM Database Mapping
- [t-005](t-005.md): 178 entries, typeorm-mysql-tuning-skill to Tzurot Deployment Guide
- [u-001](u-001.md): 1,315 entries, u to uv
- [u-002](u-002.md): 125 entries, uv to uzbekcha-spinner
- [v-001](v-001.md): 1,269 entries, v to vigil-check-2
- [v-002](v-002.md): 868 entries, vigil-incident to vz
- [w-001](w-001.md): 1,323 entries, W&B Plot Skill to whawkinsiv-solo-founder-superpowers
- [w-002](w-002.md): 1,304 entries, wheee to worktrees-skill
- [w-003](w-003.md): 580 entries, worktrunk to wzkariampuzha-claude-skills
- [x-001](x-001.md): 605 entries, x to xyo-skills
- [y-001](y-001.md): 545 entries, y-context7 to yzmir-training-optimization
- [z-001](z-001.md): 561 entries, z to zzzprobe
