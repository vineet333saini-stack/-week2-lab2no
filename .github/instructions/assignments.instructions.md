# Assignment Contribution Instructions

This document explains how to add or update an assignment for the educational portal.

## Purpose

Provide clear, well-structured assignments that are easy for students to browse, run, and download.

## Folder & file structure

Each assignment should live in its own folder under `assignments/` with a descriptive folder name (kebab-case or snake_case).

Recommended files inside the assignment folder:

- `README.md` — assignment overview, learning objectives, estimated time, and instructions for students.
- `starter-code.py` / `starter-code.<ext>` — starter files for the assignment language.
- `data.csv`, `assets/`, or other supporting files as needed.
- `solution/` (optional, for instructors) — reference solutions or test harness.

## Metadata & configuration

- Add or update the main `config.json` (project root) to include the assignment entry so the site lists it. Include fields: `id`, `title`, `path`, `difficulty`, `estimated_time`, and `tags`.
- Use the `templates/assignment-template.md` to create consistent README content.

## Content guidelines

- Learning-focused: state 2–4 clear learning objectives at the top of `README.md`.
- Student-friendly: use encouraging, simple language and provide examples where helpful.
- Difficulty: mark as `Beginner`, `Intermediate`, or `Advanced` in both the folder README and `config.json`.
- Estimated time: provide an estimate (e.g., "30–45 minutes").

## Tests & verification

- If the assignment includes automated tests, add a simple test runner (or `tests/`) and describe how to run tests in the `README.md`.
- Verify the assignment directory renders correctly by opening `index.html` locally or running your preferred static preview.

## Images & media

- Keep images in the assignment folder under `assets/images/` and reference them with relative paths.
- Optimize images for web (small file sizes) and include alt text for accessibility.

## Licensing & attribution

- Include any required attribution or license notes in the `README.md`. Prefer permissive licenses for teaching materials (e.g., CC-BY or MIT for code).

## PR checklist for contributors

- [ ] Folder named correctly and placed under `assignments/`.
- [ ] `README.md` filled using the template with learning objectives and estimated time.
- [ ] `config.json` updated (or include a config change in the PR) with required metadata.
- [ ] Starter code and supporting files are included and executable where applicable.
- [ ] Images optimized and accessible.
- [ ] Tests (if present) pass locally.

## Review & publishing

Assign a reviewer familiar with the subject matter. After approval, the assignment will appear in the portal automatically once merged to the default branch.

If you have questions or need help formatting content, open an issue in this repository and tag a maintainer.

---
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files should follow these guidelines:

## 1. Template Usage

- Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).
- The assignment must be created as a `README.md` file
- Do not remove or skip required sections from the template.

## 2. Section Guidance

The section headers should reflect the structure in the template, including the exact icon usage.

- **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
- **Objective**: Write 1-2 sentences summarizing what the student will learn or accomplish. Focus on the main skills or concepts.
- **Tasks**: For each task:
	- Use a specific, action-oriented task name
	- In the Description, clearly state what the student must do.
	- In Requirements, use bullet points to list the expected outcomes or features. Be specific and measurable
	- Provide example input/output in code blocks if helpful.

Do not include extra sections unless explicitly specified. (See <attachments> above for file contents. You may not need to search or read the file again.)
