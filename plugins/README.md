# Plugins

95,262 Claude Code plugins: every entry of every `.claude-plugin/marketplace.json` the crawl found, with what it does, where it lives and what is inside it.

## Get it

- [`plugins.csv`](plugins.csv) (34 MB)

Columns: `name`, `description`, `category`, `keywords`, `version`, `repo`, `url`, `stars`, `license`, `last_pushed`, `skills`, `commands`, `agents`, `hook_files`, `mcp_configs`, `marketplace_repo`, `marketplace_name`, `marketplaces`, `copies`, `repo_gone`.

## Notes

- Built from 113,187 marketplace entries. A plugin listed in several marketplaces appears once; copies with the same name and description under other repos (forks, mirrors) are folded into the original (`copies`).
- 81,179 have a description, in the author's words, cut at 600 characters. 1,235 of those were blank in the marketplace and filled from the plugin's own `plugin.json` or its repo description.
- `skills`, `commands`, `agents`, `hook_files`, `mcp_configs` count the files found under the plugin's folder.
- To install one: `/plugin marketplace add <marketplace_repo>` then `/plugin install <name>@<marketplace_name>`.
- 999 point at a repo that was already deleted or renamed at crawl time (`repo_gone`).
- `stars`, `license` and `last_pushed` belong to the repo, not the plugin.

## Browse

- [0-9-001](0-9-001.md): 344 entries, /api to 系统架构
- [a-001](a-001.md): 1,323 entries, a to agent-authoring
- [a-002](a-002.md): 1,373 entries, agent-authoring to agentic-readiness-assessment
- [a-003](a-003.md): 1,347 entries, agentic-repo-baseline-plugin to aigovops-community
- [a-004](a-004.md): 1,320 entries, aigovops-design to anthropic-hookify
- [a-005](a-005.md): 1,293 entries, anthropic-office-skills to arcanea
- [a-006](a-006.md): 1,316 entries, arcanea-design to auditing-compliance
- [a-007](a-007.md): 1,019 entries, auditing-deep-link-contracts to azzist
- [b-001](b-001.md): 1,361 entries, b to bitz-flow
- [b-002](b-002.md): 1,374 entries, bitz-quality to build
- [b-003](b-003.md): 451 entries, build to byunk-claude-code-toolkit
- [c-001](c-001.md): 1,394 entries, c to cds-prevention
- [c-002](c-002.md): 1,354 entries, cdt to claude-backup-sync
- [c-003](c-003.md): 1,323 entries, claude-bailian-hud to claude-skills-testing
- [c-004](c-004.md): 1,389 entries, claude-skills-updater to coach
- [c-005](c-005.md): 1,380 entries, coach to codynd
- [c-006](c-006.md): 1,353 entries, coe to constitution
- [c-007](c-007.md): 1,321 entries, constitution to cowork-mcp-tool-hook-probe
- [c-008](c-008.md): 1,326 entries, cowork-mdm to cx-atendimento
- [c-009](c-009.md): 98 entries, cx-devassist to czsc-chan-theory
- [d-001](d-001.md): 1,390 entries, d to deck-builder
- [d-002](d-002.md): 1,322 entries, deck-builder to desktop-app-dev-2
- [d-003](d-003.md): 1,309 entries, desktop-app-engineering to dfg-foerderantrag
- [d-004](d-004.md): 1,344 entries, dfir to dojo-kit
- [d-005](d-005.md): 999 entries, dojowatch to dz0ny-devenv-claude
- [e-001](e-001.md): 1,283 entries, e-colleagues to engineering-software-architect-zh
- [e-002](e-002.md): 1,331 entries, engineering-solidity-smart-contract-engineer to expert-dev-tools
- [e-003](e-003.md): 218 entries, expert-lsp to ezsub
- [f-001](f-001.md): 1,303 entries, f-awesome-chatgpt-prompts-1 to find-skills
- [f-002](f-002.md): 1,420 entries, find-skills to fountain
- [f-003](f-003.md): 835 entries, four-dx-coach to fzymgc-house-fzymgc-house-skills
- [g-001](g-001.md): 1,422 entries, g to git-commit
- [g-002](g-002.md): 1,448 entries, git-commit to google-cloud-developer
- [g-003](g-003.md): 1,325 entries, google-cloud-developer to gzp
- [h-001](h-001.md): 1,417 entries, h-mode to hivemind
- [h-002](h-002.md): 1,226 entries, hivespace to hzt
- [i-001](i-001.md): 1,282 entries, i to integrated-tools-suite
- [i-002](i-002.md): 865 entries, integration to izmailov
- [j-001](j-001.md): 1,415 entries, j-flow to jvm-languages-3
- [j-002](j-002.md): 46 entries, jvm-pulse to jyotish
- [k-001](k-001.md): 1,363 entries, k-dense-ai-claude-scientific-skills to kwdb-build
- [k-002](k-002.md): 36 entries, kwdb-data-migration to kyzo-python
- [l-001](l-001.md): 1,315 entries, l0st0-skills to lighthouse-runner
- [l-002](l-002.md): 1,365 entries, lighthouse-runner to lottie-design
- [l-003](l-003.md): 329 entries, lottie-maker to lz-advisor
- [m-001](m-001.md): 1,297 entries, m to mastering-aws-cdk
- [m-002](m-002.md): 1,409 entries, mastering-gemini-cli to mesh-observe
- [m-003](m-003.md): 1,341 entries, mesh-recon to model-first-reasoning
- [m-004](m-004.md): 1,177 entries, model-gateway to mzizzi-ty-lsp
- [n-001](n-001.md): 1,301 entries, n to node-onboarding
- [n-002](n-002.md): 708 entries, node-rpm to nzism-tanaji-hemant-naik
- [o-001](o-001.md): 1,410 entries, o-m-cc to openai-security-ownership-map
- [o-002](o-002.md): 1,320 entries, openai-security-threat-model to owasp-compliance-checker-2
- [o-003](o-003.md): 51 entries, owasp-compliance-checker-3 to ozma
- [p-001](p-001.md): 1,366 entries, p to personal-finance
- [p-002](p-002.md): 1,389 entries, personal-finance-coach to plugin-doctor
- [p-003](p-003.md): 1,386 entries, plugin-editor to ppbp-alm
- [p-004](p-004.md): 1,300 entries, ppbp-codeapps to product-video
- [p-005](p-005.md): 1,313 entries, product-video to pulser-odoo
- [p-006](p-006.md): 455 entries, pulumi to pyzotero
- [q-001](q-001.md): 724 entries, q to qyrusai-assure
- [r-001](r-001.md): 1,352 entries, r to reflect
- [r-002](r-002.md): 1,343 entries, reflect to retail-reason
- [r-003](r-003.md): 1,356 entries, retail-store-operations to rule-deviation-mapper-resolve
- [r-004](r-004.md): 315 entries, rule-enforcement-audit to rzpro
- [s-001](s-001.md): 1,245 entries, s to scrumia-kotlin-multiplatform-mobile
- [s-002](s-002.md): 1,322 entries, scrumia-ktor to seo-geo
- [s-003](s-003.md): 1,401 entries, seo-geo to sideshow
- [s-004](s-004.md): 1,395 entries, sids-airbot to slang-lsp
- [s-005](s-005.md): 1,292 entries, slant to spec-generator
- [s-006](s-006.md): 1,405 entries, spec-generator to stm32
- [s-007](s-007.md): 1,328 entries, stm32-debug-kit to swarmdo-federation
- [s-008](s-008.md): 579 entries, swarmdo-goals to sztwiorok-buddy-plugin
- [t-001](t-001.md): 1,360 entries, t-view-automation to terminal-firefox-skill
- [t-002](t-002.md): 1,376 entries, terminal-guru to tisax
- [t-003](t-003.md): 1,397 entries, tischlein to truinorva-triz
- [t-004](t-004.md): 567 entries, truist-credit-memo-agent to tzevaadom-alerts-suite
- [u-001](u-001.md): 1,197 entries, u to uzbekcha-spinner
- [v-001](v-001.md): 1,301 entries, v to vivarium-a2a-simulation
- [v-002](v-002.md): 506 entries, viver-de-ia to vz
- [w-001](w-001.md): 1,337 entries, wa to windsock
- [w-002](w-002.md): 1,375 entries, windsor-ai to wycena-automatyzacji
- [w-003](w-003.md): 4 entries, wyre-gateway to wzkariampuzha-claude-skills
- [x-001](x-001.md): 528 entries, x to xyo-skills
- [y-001](y-001.md): 471 entries, y-context7 to yzmir-training-optimization
- [z-001](z-001.md): 496 entries, z to zzzprobe
