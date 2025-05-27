import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "GeoNetwork Workshop",
  description:
    "This website will take you through various steps to help you discover GeoNetwork.",
  themeConfig: {
    logo: {
      src: "/geonetwork-logo.svg",
      alt: "GeoNetwork logo",
    },
    sidebar: [
      {
        text: "Basics",
        items: [
          { text: "Getting Started", link: "/getting-started" },
          { text: "Overview", link: "/overview" },
          { text: "Deploying GeoNetwork", link: "/deploying" },
          { text: "Administration", link: "/administration" },
          { text: "Adding Records", link: "/adding-records" },
          // { text: "Managing Records", link: "/managing-records" },
        ],
      },
      { text: "Intermission", link: "/intermission" },
      {
        text: "GeoNetwork-UI",
        items: [
          { text: "Overview", link: "/gnui-overview" },
          { text: "Deploying the Datahub", link: "/deploying-datahub" },
          { text: "Deploying the Metadata Editor", link: "/deploying-editor" },
        ],
      },
      {
        text: "Common Issues",
        link: "/common-issues",
      },
      {
        text: `<div style="height: calc(100vh - 760px);"></div>`,
      },
      {
        text: "<a href='https://www.camptocamp.com'><small>Made with <img src='/gs-workshop-geonetwork/c2c-logo.png' alt='Camptocamp logo' style='display: inline; width: 21px; vertical-align: middle;' /> by <strong>Camptocamp</strong></small></a>",
      },
    ],

    nav: [
      {
        text: "GeoNetwork Website",
        link: "https://geonetwork-opensource.org/",
      },
      {
        text: "GeoNetwork Documentation",
        link: "https://docs.geonetwork-opensource.org/4.4/",
      },
    ],
    footer: {
      message:
        "<span>Made with <img src='/gs-workshop-geonetwork/c2c-logo.png' alt='Camptocamp logo' style='display: inline; width: 22px; vertical-align: middle;' /> by <a href='https://www.camptocamp.com'>Camptocamp</a></span>",
      copyright: "Copyright © 2025-present",
    },
  },

  locales: {
    root: {
      label: "English",
      lang: "en",
    },
    de: {
      label: "German",
      lang: "de",
      link: "/de/",
      themeConfig: {
        sidebar: [
          {
            text: "Grundlagen",
            items: [
              { text: "Erste Schritte", link: "/de/getting-started" },
              { text: "Überblick", link: "/de/overview" },
              { text: "GeoNetwork Deployment", link: "/de/deploying" },
              { text: "Administration", link: "/de/administration" },
              { text: "Datensätze hinzufügen", link: "/de/adding-records" },
            ],
          },
          { text: "Zwischenpause", link: "/de/intermission" },
          {
            text: "GeoNetwork-UI",
            items: [
              { text: "Überblick", link: "/de/gnui-overview" },
              {
                text: "Datahub Deployment",
                link: "/de/deploying-datahub",
              },
              {
                text: "Metadaten-Editor Deployment",
                link: "/de/deploying-editor",
              },
            ],
          },
          {
            text: "Häufige Probleme",
            link: "/common-issues",
          },
          {
            text: `<div style="height: calc(100vh - 760px);"></div>`,
          },
          {
            text: "<a href='https://www.camptocamp.com'><small>Erstellt mit <img src='/gs-workshop-geonetwork/c2c-logo.png' alt='Camptocamp Logo' style='display: inline; width: 21px; vertical-align: middle;' /> von <strong>Camptocamp</strong></small></a>",
          },
        ],
      },
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
