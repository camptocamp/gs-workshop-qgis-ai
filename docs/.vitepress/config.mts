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
        text: "Introduction", link: "/introduction"
      },
      {
        text: "Démarrage", link: "/getting-started"
      },
      {
        text: "1. Chatbots web",
        items: [
          { text: "Contexte", link: "/chat_intro" },
          { text: "Use case", link: "/chat_usecase1" },
        ],
      },
      {
        text: "QGIS plugins",
        items: [
          { text: "Plugins", link: "/plugins_list" },
        ],
      },
      {
        text: "MCP servers",
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
        link: "./introduction",
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
        href: "/gs-workshop-geonetwork/geonetwork-logo.svg",
      },
    ],
  ], // this will work when deployed on GH Pages

  ignoreDeadLinks: [
    // ignore all localhost links
    /^https?:\/\/localhost/,
  ],
});
