# Deploy RACV Dashboard to Azure Static Web Apps

Two deployment options. Choose whichever matches your access level.

---

## OPTION A: GitHub Integration (Recommended -- Automated)

### Prerequisites
- Azure subscription with contributor access
- GitHub access (to the racv-travel-dashboard repo)

### Steps

1. **Create the Azure Static Web App**
   - Go to the Azure Portal -> Create a resource -> Static Web App
   - Resource group: create new, e.g. `rg-racv-dashboard`
   - Name: `racv-travel-dashboard`
   - Plan: **Free** (100 GB bandwidth/month, enough for this use)
   - Region: Australia East (Sydney)
   - Deployment details:
     - Source: **GitHub**
     - Sign in and select organization `gtghome`
     - Repository: `racv-travel-dashboard`
     - Branch: `main`
   - Build Details:
     - Build Preset: **Custom**
     - App location: `/public`
     - API location: (leave blank)
     - Output location: (leave blank)
   - Review + create.

2. **Azure auto-generates the workflow file**
   During creation, Azure commits `.github/workflows/azure-static-web-apps-XXX.yml` to your repo and adds a secret `AZURE_STATIC_WEB_APPS_API_TOKEN` to GitHub.
   
   We already have a workflow file at `.github/workflows/azure-static-web-apps.yml`. Either:
   - **Let Azure create its own file** (it will, alongside our one). Delete ours afterwards. OR
   - **Skip automatic workflow creation**: when creating the SWA, choose "Other" for source, then manually add the `AZURE_STATIC_WEB_APPS_API_TOKEN` secret to GitHub and our existing workflow will be used.

3. **First deployment**
   On next push to `main` (or manually trigger the workflow), the dashboard deploys automatically.

4. **Custom domain (optional)**
   Azure SWA URL will be something like `https://gentle-pond-abc123.australiaeast-1.azurestaticapps.net`.
   To use a custom domain (e.g. `dashboard.racv-gtg.com`):
   - In the SWA resource, go to Custom domains
   - Add your domain
   - Add the CNAME record to your DNS

---

## OPTION B: Manual ZIP Upload via Azure CLI

If you don't have GitHub integration or want a one-off deploy:

### Prerequisites
- Azure CLI installed (`az --version`)
- `swa` CLI installed (`npm install -g @azure/static-web-apps-cli`)

### Steps

1. **Download the Azure-ready ZIP** 
   Use the file `racv-dashboard-azure-ready.zip` (shared separately in this conversation). Unzip to a folder, e.g. `./racv-dashboard-public/`.

2. **Log into Azure**
   ```bash
   az login
   az account set --subscription "<your-subscription-id>"
   ```

3. **Create the Static Web App (one-time)**
   ```bash
   az staticwebapp create \
     --name racv-travel-dashboard \
     --resource-group rg-racv-dashboard \
     --location australiaeast \
     --sku Free
   ```

4. **Get the deployment token**
   ```bash
   az staticwebapp secrets list \
     --name racv-travel-dashboard \
     --resource-group rg-racv-dashboard \
     --query "properties.apiKey" -o tsv
   ```
   Copy this token.

5. **Deploy using SWA CLI**
   ```bash
   cd racv-dashboard-public
   swa deploy . \
     --deployment-token <paste-token-here> \
     --env production
   ```

6. **Find your URL**
   ```bash
   az staticwebapp show \
     --name racv-travel-dashboard \
     --resource-group rg-racv-dashboard \
     --query "defaultHostname" -o tsv
   ```

---

## OPTION C: Azure Portal Drag-and-Drop (Easiest, No CLI)

1. Create Static Web App in Azure Portal (same as Option A step 1) but choose **"Other"** as deployment source.
2. In the created SWA resource, go to **Overview > Manage deployment token** -> copy token.
3. Go to **Deployment Center** or use the following browser-based method:
   - Unzip `racv-dashboard-azure-ready.zip` locally
   - Use Azure Portal's **Upload** function under Deployment
   - Drag the contents of the `public/` folder

OR use Visual Studio Code:
- Install the "Azure Static Web Apps" extension
- Right-click `public/` folder -> "Deploy to Static Web App"
- Authenticate and select your SWA resource

---

## Configuration Already Included

The `public/` folder includes `staticwebapp.config.json` which handles:

- **SPA routing fallback** -> all routes redirect to index.html
- **Security headers** -> X-Frame-Options, CSP, Referrer-Policy
- **MIME types** -> correct content-type headers
- **Noindex** -> already in the HTML `<head>` so search engines ignore this URL

No further configuration is needed.

---

## Files in /public Folder

- `index.html` -- full dashboard (~1.5 MB, 24,000+ lines)
- `styles.css` -- dashboard styling
- `staticwebapp.config.json` -- Azure routing and security config

## Troubleshooting

**Firewall still blocks:** if `*.azurestaticapps.net` is also blocked at your org, ask IT to allow the single hostname Azure assigns you (e.g. `gentle-pond-abc123.australiaeast-1.azurestaticapps.net`).

**CORS errors:** Not applicable -- dashboard is self-contained with no external API calls.

**Slow first load:** Azure SWA's free tier has 10-second cold-start. Use paid tier (~$9 USD/month) for always-warm hosting.

**Auth:** The `/public/` version has NO login required. If you want SSO/AD authentication, configure Azure AD in Static Web App settings and add an auth block to `staticwebapp.config.json`.
