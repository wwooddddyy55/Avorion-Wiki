# publish-wiki.ps1
# Copies wiki/pages/ content to the GitHub wiki repo and pushes.
# Run from anywhere — paths are resolved relative to this script's location.

$ErrorActionPreference = "Stop"

$scriptDir   = Split-Path -Parent $MyInvocation.MyCommand.Definition
$pagesDir    = Join-Path $scriptDir "wiki\pages"
$wikiRepoUrl = "https://github.com/wwooddddyy55/Avorion-Wiki.wiki.git"
$wikiClone   = Join-Path $scriptDir "wiki\.wiki-publish"

# ── 1. Clone or update the wiki repo ────────────────────────────────────────
if (Test-Path $wikiClone) {
    Write-Host "Updating existing wiki clone..."
    git -C $wikiClone pull --ff-only
} else {
    Write-Host "Cloning wiki repo..."
    git clone $wikiRepoUrl $wikiClone
}

# ── 2. Copy all .md files from wiki/pages/ into the wiki repo ───────────────
Write-Host "Copying pages..."
Get-ChildItem -Path $pagesDir -Filter "*.md" | ForEach-Object {
    Copy-Item -Path $_.FullName -Destination $wikiClone -Force
    Write-Host "  $($_.Name)"
}

# ── 3. Stage, commit, and push ───────────────────────────────────────────────
$status = git -C $wikiClone status --porcelain
if (-not $status) {
    Write-Host "No changes to publish — wiki is already up to date."
    exit 0
}

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$commitMsg = "Sync wiki pages from main repo ($timestamp)"

git -C $wikiClone add -A
git -C $wikiClone commit -m $commitMsg
git -C $wikiClone push

Write-Host ""
Write-Host "Done. Wiki published: https://github.com/wwooddddyy55/Avorion-Wiki/wiki"
