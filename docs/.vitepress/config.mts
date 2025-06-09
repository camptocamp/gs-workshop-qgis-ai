import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "AI Workshop",
  description:
    "This website will take you through various steps to help you use LLM assistant for QGIS.",
  themeConfig: {
    logo: {
      src: "./qgis.png",
      alt: "QGIS logo",
    },
    sidebar: [
      {
        text: "Introduction", link: "/00_introduction"
      },
      {
        text: "Get started", link: "/01_getting-started"
      },
      {
        text: "1. Chatbots web",
        items: [
          { text: "Présentation Chatbots", link: "/10_chat_intro" },
          { text: "Créer un script", link: "/11_chat_create" },
          { text: "Modifier votre script", link: "/12_chat_modify" },
          { text: "Déployer un plugin", link: "/13_chat_plugin" },
        ],
      },
      {
        text: "2. QGIS plugins",
        items: [
          { text: "RAG", link: "/20_plugins_rag" },
          { text: "Liste de plugins", link: "/20_plugins_list" },
          { text: "Intelligeo", link: "/21_plugins_intelligeo" },
          { text: "Promptly", link: "/22_plugins_promptly" },
        ],
      },
      {
        text: "3. MCP servers",
        items: [
          { text: "Setup", link: "/mcp_setup" },
          { text: "Use cases", link: "/mcp_usecases" },
          { text: "Conclusion / Echange", link: "/mcp_conclusion" },
        ],
      },
      {
        text: `<div style="height: calc(100vh - 760px);"></div>`,
      },
      {
        text: "<a href='https://www.camptocamp.com'><small>Made with <img src='./c2c-logo.png' alt='Camptocamp logo' style='display: inline; width: 21px; vertical-align: middle;' /> by <strong>Camptocamp</strong></small></a>",
      },
    ],

    nav: [
      {
        text: "Workshop",
        link: "./00_introduction",
      },
      {
        text: "QGIS Website",
        link: "https://qgis.org/",
      },
      {
        text: "QGIS Documentation",
        link: "https://docs.qgis.org/3.40/en/docs/",
      },
    ],
    footer: {
      message:
        "<span>Made with <img src='./c2c-logo.png' alt='Camptocamp logo' style='display: inline; width: 22px; vertical-align: middle;' /> by <a href='https://www.camptocamp.com'>Camptocamp</a></span>",
      copyright: "Copyright © 2025-present",
    },
  },
  head: [
    [
      "link",
      {
        rel: "icon",
        href: "./favicon.png",
      },
    ],
  ], // this will work when deployed on GH Pages

  ignoreDeadLinks: [
    // ignore all localhost links
    /^https?:\/\/localhost/,
  ],
});
