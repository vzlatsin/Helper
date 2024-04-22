

### Step 1: Sign in to Google
- **Open your web browser** and navigate to the Google Developer Console at [Google Cloud Console](https://console.cloud.google.com/).
- **Sign in** with your Google account credentials. If you don’t have a Google account, you’ll need to create one.

### Step 2: Create a New Project
Once you're logged in:
- You'll see the Google Cloud Dashboard. If you're new to Google Cloud, it might ask you to agree to Terms of Service.
- **Create a new project** by clicking on the project dropdown near the top right corner next to "Google Cloud Platform". This dropdown shows your current project. Click on it, then select “New Project”.

  ![Create a New Project](https://storage.googleapis.com/support-kms-prod/SNP_2962068_en_v0)

- You’ll be prompted to **enter a project name** and optionally adjust the project ID. Once you’ve configured your settings, click “Create”.

### Step 3: Enable the Gmail API
After your project is created:
- You will be directed back to the Dashboard. Now, you need to enable the Gmail API for your project.
- Navigate to the **Navigation Menu** (hamburger menu in the top left corner) and select **APIs & Services > Library**.

  ![API Library](https://developers.google.com/maps/documentation/images/utility-gmp-get-started-enable-apis-and-services.png)

- In the API Library, **search for “Gmail API”** using the search bar.
- Click on the Gmail API in the list, then click **“Enable”** to activate the API for your project.

### Step 4: Create Credentials
After enabling the API:
- You'll be prompted to create credentials that your application will use to access the Gmail API.
- Go to **“Credentials”** in the API & Services menu.
- Click **“Create Credentials”** at the top of the page and select **“OAuth client ID”**.

  ![Create Credentials](https://developers.google.com/workspace/guides/images/create-credentials-clientid.png)

- You may be prompted to configure the **OAuth consent screen**. Fill in the required fields like the application name, email, and logo, which will be shown to users when they log in via Google.

- After configuring the consent screen, choose the application type (usually “Web application” or “Other”), and provide details such as the name and redirect URIs (where Google will send users after they authorize your application).

- Once completed, Google will provide you with a **client ID** and **client secret**. Keep these confidential as they are used to authenticate requests to Google on behalf of your application.

### Step 5: Start Developing
- With the API enabled and your credentials set up, you can start building your application using the Gmail API. You'll use the client ID and secret in your application to handle authentication via OAuth 2.0.

