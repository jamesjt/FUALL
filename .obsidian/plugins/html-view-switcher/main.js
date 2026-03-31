var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => ViewSwitcherPlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian = require("obsidian");
var VIEW_TYPE_RENDERED = "html-view";
var VIEW_TYPE_SOURCE = "vscode-editor";
var ICON_SOURCE = "code";
var ICON_RENDERED = "eye";
var ViewSwitcherPlugin = class extends import_obsidian.Plugin {
  constructor() {
    super(...arguments);
    this.actionButtons = /* @__PURE__ */ new Map();
  }
  async onload() {
    this.addCommand({
      id: "toggle-html-view",
      name: "Toggle HTML view (source \u2194 rendered)",
      checkCallback: (checking) => {
        const file = this.app.workspace.getActiveFile();
        const leaf = this.app.workspace.activeLeaf;
        if (!file || !leaf || !this.isHtmlFile(file)) return false;
        if (!checking) {
          this.toggleView(leaf, file);
        }
        return true;
      }
    });
    this.addCommand({
      id: "open-html-source-split",
      name: "Open HTML source in split pane",
      checkCallback: (checking) => {
        const file = this.app.workspace.getActiveFile();
        if (!file || !this.isHtmlFile(file)) return false;
        if (!checking) {
          this.openInSplit(file, VIEW_TYPE_SOURCE);
        }
        return true;
      }
    });
    this.addCommand({
      id: "open-html-rendered-split",
      name: "Open HTML rendered in split pane",
      checkCallback: (checking) => {
        const file = this.app.workspace.getActiveFile();
        if (!file || !this.isHtmlFile(file)) return false;
        if (!checking) {
          this.openInSplit(file, VIEW_TYPE_RENDERED);
        }
        return true;
      }
    });
    this.addCommand({
      id: "open-html-side-by-side",
      name: "Open HTML side by side (source + rendered)",
      checkCallback: (checking) => {
        const file = this.app.workspace.getActiveFile();
        if (!file || !this.isHtmlFile(file)) return false;
        if (!checking) {
          this.openSideBySide(file);
        }
        return true;
      }
    });
    this.registerEvent(
      this.app.workspace.on("active-leaf-change", (leaf) => {
        this.updateAllButtons();
      })
    );
    this.registerEvent(
      this.app.workspace.on("layout-change", () => {
        this.updateAllButtons();
      })
    );
    this.app.workspace.onLayoutReady(() => {
      this.updateAllButtons();
    });
  }
  onunload() {
    this.actionButtons.forEach((btn, leaf) => {
      btn.detach();
    });
    this.actionButtons.clear();
  }
  isHtmlFile(file) {
    const ext = file.extension.toLowerCase();
    return ["html", "htm", "mhtml", "mht"].includes(ext);
  }
  isHtmlView(leaf) {
    const viewType = leaf.view.getViewType();
    return viewType === VIEW_TYPE_RENDERED || viewType === VIEW_TYPE_SOURCE;
  }
  updateAllButtons() {
    const currentLeaves = /* @__PURE__ */ new Set();
    this.app.workspace.iterateAllLeaves((leaf) => {
      currentLeaves.add(leaf);
      if (this.isHtmlView(leaf)) {
        if (!this.actionButtons.has(leaf)) {
          this.addToggleButton(leaf);
        } else {
          this.updateButtonIcon(leaf);
        }
      } else {
        this.removeButton(leaf);
      }
    });
    this.actionButtons.forEach((btn, leaf) => {
      if (!currentLeaves.has(leaf)) {
        btn.detach();
        this.actionButtons.delete(leaf);
      }
    });
  }
  addToggleButton(leaf) {
    const view = leaf.view;
    if (!view.addAction) return;
    const currentType = view.getViewType();
    const icon = currentType === VIEW_TYPE_SOURCE ? ICON_RENDERED : ICON_SOURCE;
    const tooltip = currentType === VIEW_TYPE_SOURCE ? "Switch to rendered view" : "Switch to source view";
    const btn = view.addAction(icon, tooltip, () => {
      const file = view.file;
      if (file) {
        this.toggleView(leaf, file);
      }
    });
    this.actionButtons.set(leaf, btn);
  }
  updateButtonIcon(leaf) {
    this.removeButton(leaf);
    this.addToggleButton(leaf);
  }
  removeButton(leaf) {
    const btn = this.actionButtons.get(leaf);
    if (btn) {
      btn.detach();
      this.actionButtons.delete(leaf);
    }
  }
  async openInSplit(file, viewType) {
    const leaf = this.app.workspace.getLeaf("split");
    await leaf.setViewState({
      type: viewType,
      state: { file: file.path }
    });
    this.app.workspace.revealLeaf(leaf);
  }
  async openSideBySide(file) {
    const currentLeaf = this.app.workspace.activeLeaf;
    const currentType = currentLeaf == null ? void 0 : currentLeaf.view.getViewType();
    if (currentLeaf && currentType !== VIEW_TYPE_RENDERED) {
      await currentLeaf.setViewState({
        type: VIEW_TYPE_RENDERED,
        state: { file: file.path }
      });
    }
    const newLeaf = this.app.workspace.getLeaf("split");
    await newLeaf.setViewState({
      type: VIEW_TYPE_SOURCE,
      state: { file: file.path }
    });
    this.app.workspace.revealLeaf(newLeaf);
  }
  async toggleView(leaf, file) {
    const currentType = leaf.view.getViewType();
    const newType = currentType === VIEW_TYPE_SOURCE ? VIEW_TYPE_RENDERED : VIEW_TYPE_SOURCE;
    await leaf.setViewState({
      type: newType,
      state: { file: file.path }
    });
  }
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsic3JjL21haW4udHMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImltcG9ydCB7XG4gIFBsdWdpbixcbiAgV29ya3NwYWNlTGVhZixcbiAgVEZpbGUsXG4gIEl0ZW1WaWV3LFxufSBmcm9tIFwib2JzaWRpYW5cIjtcblxuY29uc3QgVklFV19UWVBFX1JFTkRFUkVEID0gXCJodG1sLXZpZXdcIjtcbmNvbnN0IFZJRVdfVFlQRV9TT1VSQ0UgPSBcInZzY29kZS1lZGl0b3JcIjtcbmNvbnN0IElDT05fU09VUkNFID0gXCJjb2RlXCI7XG5jb25zdCBJQ09OX1JFTkRFUkVEID0gXCJleWVcIjtcblxuZXhwb3J0IGRlZmF1bHQgY2xhc3MgVmlld1N3aXRjaGVyUGx1Z2luIGV4dGVuZHMgUGx1Z2luIHtcbiAgcHJpdmF0ZSBhY3Rpb25CdXR0b25zOiBNYXA8V29ya3NwYWNlTGVhZiwgSFRNTEVsZW1lbnQ+ID0gbmV3IE1hcCgpO1xuXG4gIGFzeW5jIG9ubG9hZCgpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICAvLyBUb2dnbGUgY29tbWFuZCAodXNlciBhc3NpZ25zIGhvdGtleSBpbiBTZXR0aW5ncyBcdTIxOTIgSG90a2V5cylcbiAgICB0aGlzLmFkZENvbW1hbmQoe1xuICAgICAgaWQ6IFwidG9nZ2xlLWh0bWwtdmlld1wiLFxuICAgICAgbmFtZTogXCJUb2dnbGUgSFRNTCB2aWV3IChzb3VyY2UgXHUyMTk0IHJlbmRlcmVkKVwiLFxuICAgICAgY2hlY2tDYWxsYmFjazogKGNoZWNraW5nOiBib29sZWFuKSA9PiB7XG4gICAgICAgIGNvbnN0IGZpbGUgPSB0aGlzLmFwcC53b3Jrc3BhY2UuZ2V0QWN0aXZlRmlsZSgpO1xuICAgICAgICBjb25zdCBsZWFmID0gdGhpcy5hcHAud29ya3NwYWNlLmFjdGl2ZUxlYWY7XG4gICAgICAgIGlmICghZmlsZSB8fCAhbGVhZiB8fCAhdGhpcy5pc0h0bWxGaWxlKGZpbGUpKSByZXR1cm4gZmFsc2U7XG4gICAgICAgIGlmICghY2hlY2tpbmcpIHtcbiAgICAgICAgICB0aGlzLnRvZ2dsZVZpZXcobGVhZiwgZmlsZSk7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9LFxuICAgIH0pO1xuXG4gICAgLy8gU3BsaXQgcGFuZSBjb21tYW5kc1xuICAgIHRoaXMuYWRkQ29tbWFuZCh7XG4gICAgICBpZDogXCJvcGVuLWh0bWwtc291cmNlLXNwbGl0XCIsXG4gICAgICBuYW1lOiBcIk9wZW4gSFRNTCBzb3VyY2UgaW4gc3BsaXQgcGFuZVwiLFxuICAgICAgY2hlY2tDYWxsYmFjazogKGNoZWNraW5nOiBib29sZWFuKSA9PiB7XG4gICAgICAgIGNvbnN0IGZpbGUgPSB0aGlzLmFwcC53b3Jrc3BhY2UuZ2V0QWN0aXZlRmlsZSgpO1xuICAgICAgICBpZiAoIWZpbGUgfHwgIXRoaXMuaXNIdG1sRmlsZShmaWxlKSkgcmV0dXJuIGZhbHNlO1xuICAgICAgICBpZiAoIWNoZWNraW5nKSB7XG4gICAgICAgICAgdGhpcy5vcGVuSW5TcGxpdChmaWxlLCBWSUVXX1RZUEVfU09VUkNFKTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0sXG4gICAgfSk7XG5cbiAgICB0aGlzLmFkZENvbW1hbmQoe1xuICAgICAgaWQ6IFwib3Blbi1odG1sLXJlbmRlcmVkLXNwbGl0XCIsXG4gICAgICBuYW1lOiBcIk9wZW4gSFRNTCByZW5kZXJlZCBpbiBzcGxpdCBwYW5lXCIsXG4gICAgICBjaGVja0NhbGxiYWNrOiAoY2hlY2tpbmc6IGJvb2xlYW4pID0+IHtcbiAgICAgICAgY29uc3QgZmlsZSA9IHRoaXMuYXBwLndvcmtzcGFjZS5nZXRBY3RpdmVGaWxlKCk7XG4gICAgICAgIGlmICghZmlsZSB8fCAhdGhpcy5pc0h0bWxGaWxlKGZpbGUpKSByZXR1cm4gZmFsc2U7XG4gICAgICAgIGlmICghY2hlY2tpbmcpIHtcbiAgICAgICAgICB0aGlzLm9wZW5JblNwbGl0KGZpbGUsIFZJRVdfVFlQRV9SRU5ERVJFRCk7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9LFxuICAgIH0pO1xuXG4gICAgLy8gU2lkZS1ieS1zaWRlIGNvbW1hbmRcbiAgICB0aGlzLmFkZENvbW1hbmQoe1xuICAgICAgaWQ6IFwib3Blbi1odG1sLXNpZGUtYnktc2lkZVwiLFxuICAgICAgbmFtZTogXCJPcGVuIEhUTUwgc2lkZSBieSBzaWRlIChzb3VyY2UgKyByZW5kZXJlZClcIixcbiAgICAgIGNoZWNrQ2FsbGJhY2s6IChjaGVja2luZzogYm9vbGVhbikgPT4ge1xuICAgICAgICBjb25zdCBmaWxlID0gdGhpcy5hcHAud29ya3NwYWNlLmdldEFjdGl2ZUZpbGUoKTtcbiAgICAgICAgaWYgKCFmaWxlIHx8ICF0aGlzLmlzSHRtbEZpbGUoZmlsZSkpIHJldHVybiBmYWxzZTtcbiAgICAgICAgaWYgKCFjaGVja2luZykge1xuICAgICAgICAgIHRoaXMub3BlblNpZGVCeVNpZGUoZmlsZSk7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9LFxuICAgIH0pO1xuXG4gICAgLy8gQWRkIHRvZ2dsZSBidXR0b24gdG8gdmlldyBoZWFkZXJzIHdoZW4gSFRNTCBmaWxlcyBhcmUgYWN0aXZlXG4gICAgdGhpcy5yZWdpc3RlckV2ZW50KFxuICAgICAgdGhpcy5hcHAud29ya3NwYWNlLm9uKFwiYWN0aXZlLWxlYWYtY2hhbmdlXCIsIChsZWFmKSA9PiB7XG4gICAgICAgIHRoaXMudXBkYXRlQWxsQnV0dG9ucygpO1xuICAgICAgfSlcbiAgICApO1xuXG4gICAgdGhpcy5yZWdpc3RlckV2ZW50KFxuICAgICAgdGhpcy5hcHAud29ya3NwYWNlLm9uKFwibGF5b3V0LWNoYW5nZVwiLCAoKSA9PiB7XG4gICAgICAgIHRoaXMudXBkYXRlQWxsQnV0dG9ucygpO1xuICAgICAgfSlcbiAgICApO1xuXG4gICAgLy8gSW5pdGlhbCBidXR0b24gc2V0dXBcbiAgICB0aGlzLmFwcC53b3Jrc3BhY2Uub25MYXlvdXRSZWFkeSgoKSA9PiB7XG4gICAgICB0aGlzLnVwZGF0ZUFsbEJ1dHRvbnMoKTtcbiAgICB9KTtcbiAgfVxuXG4gIG9udW5sb2FkKCk6IHZvaWQge1xuICAgIC8vIENsZWFuIHVwIGFsbCBidXR0b25zXG4gICAgdGhpcy5hY3Rpb25CdXR0b25zLmZvckVhY2goKGJ0biwgbGVhZikgPT4ge1xuICAgICAgYnRuLmRldGFjaCgpO1xuICAgIH0pO1xuICAgIHRoaXMuYWN0aW9uQnV0dG9ucy5jbGVhcigpO1xuICB9XG5cbiAgcHJpdmF0ZSBpc0h0bWxGaWxlKGZpbGU6IFRGaWxlKTogYm9vbGVhbiB7XG4gICAgY29uc3QgZXh0ID0gZmlsZS5leHRlbnNpb24udG9Mb3dlckNhc2UoKTtcbiAgICByZXR1cm4gW1wiaHRtbFwiLCBcImh0bVwiLCBcIm1odG1sXCIsIFwibWh0XCJdLmluY2x1ZGVzKGV4dCk7XG4gIH1cblxuICBwcml2YXRlIGlzSHRtbFZpZXcobGVhZjogV29ya3NwYWNlTGVhZik6IGJvb2xlYW4ge1xuICAgIGNvbnN0IHZpZXdUeXBlID0gbGVhZi52aWV3LmdldFZpZXdUeXBlKCk7XG4gICAgcmV0dXJuIHZpZXdUeXBlID09PSBWSUVXX1RZUEVfUkVOREVSRUQgfHwgdmlld1R5cGUgPT09IFZJRVdfVFlQRV9TT1VSQ0U7XG4gIH1cblxuICBwcml2YXRlIHVwZGF0ZUFsbEJ1dHRvbnMoKTogdm9pZCB7XG4gICAgLy8gVHJhY2sgd2hpY2ggbGVhdmVzIHN0aWxsIGV4aXN0XG4gICAgY29uc3QgY3VycmVudExlYXZlcyA9IG5ldyBTZXQ8V29ya3NwYWNlTGVhZj4oKTtcblxuICAgIHRoaXMuYXBwLndvcmtzcGFjZS5pdGVyYXRlQWxsTGVhdmVzKChsZWFmKSA9PiB7XG4gICAgICBjdXJyZW50TGVhdmVzLmFkZChsZWFmKTtcblxuICAgICAgaWYgKHRoaXMuaXNIdG1sVmlldyhsZWFmKSkge1xuICAgICAgICBpZiAoIXRoaXMuYWN0aW9uQnV0dG9ucy5oYXMobGVhZikpIHtcbiAgICAgICAgICB0aGlzLmFkZFRvZ2dsZUJ1dHRvbihsZWFmKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAvLyBVcGRhdGUgaWNvbiB0byByZWZsZWN0IGN1cnJlbnQgc3RhdGVcbiAgICAgICAgICB0aGlzLnVwZGF0ZUJ1dHRvbkljb24obGVhZik7XG4gICAgICAgIH1cbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIC8vIE5vdCBhbiBIVE1MIHZpZXcsIHJlbW92ZSBidXR0b24gaWYgaXQgZXhpc3RzXG4gICAgICAgIHRoaXMucmVtb3ZlQnV0dG9uKGxlYWYpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgLy8gQ2xlYW4gdXAgYnV0dG9ucyBmb3IgbGVhdmVzIHRoYXQgbm8gbG9uZ2VyIGV4aXN0XG4gICAgdGhpcy5hY3Rpb25CdXR0b25zLmZvckVhY2goKGJ0biwgbGVhZikgPT4ge1xuICAgICAgaWYgKCFjdXJyZW50TGVhdmVzLmhhcyhsZWFmKSkge1xuICAgICAgICBidG4uZGV0YWNoKCk7XG4gICAgICAgIHRoaXMuYWN0aW9uQnV0dG9ucy5kZWxldGUobGVhZik7XG4gICAgICB9XG4gICAgfSk7XG4gIH1cblxuICBwcml2YXRlIGFkZFRvZ2dsZUJ1dHRvbihsZWFmOiBXb3Jrc3BhY2VMZWFmKTogdm9pZCB7XG4gICAgY29uc3QgdmlldyA9IGxlYWYudmlldyBhcyBJdGVtVmlldztcbiAgICBpZiAoIXZpZXcuYWRkQWN0aW9uKSByZXR1cm47XG5cbiAgICBjb25zdCBjdXJyZW50VHlwZSA9IHZpZXcuZ2V0Vmlld1R5cGUoKTtcbiAgICBjb25zdCBpY29uID0gY3VycmVudFR5cGUgPT09IFZJRVdfVFlQRV9TT1VSQ0UgPyBJQ09OX1JFTkRFUkVEIDogSUNPTl9TT1VSQ0U7XG4gICAgY29uc3QgdG9vbHRpcCA9XG4gICAgICBjdXJyZW50VHlwZSA9PT0gVklFV19UWVBFX1NPVVJDRVxuICAgICAgICA/IFwiU3dpdGNoIHRvIHJlbmRlcmVkIHZpZXdcIlxuICAgICAgICA6IFwiU3dpdGNoIHRvIHNvdXJjZSB2aWV3XCI7XG5cbiAgICBjb25zdCBidG4gPSB2aWV3LmFkZEFjdGlvbihpY29uLCB0b29sdGlwLCAoKSA9PiB7XG4gICAgICBjb25zdCBmaWxlID0gKHZpZXcgYXMgYW55KS5maWxlIGFzIFRGaWxlO1xuICAgICAgaWYgKGZpbGUpIHtcbiAgICAgICAgdGhpcy50b2dnbGVWaWV3KGxlYWYsIGZpbGUpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgdGhpcy5hY3Rpb25CdXR0b25zLnNldChsZWFmLCBidG4pO1xuICB9XG5cbiAgcHJpdmF0ZSB1cGRhdGVCdXR0b25JY29uKGxlYWY6IFdvcmtzcGFjZUxlYWYpOiB2b2lkIHtcbiAgICB0aGlzLnJlbW92ZUJ1dHRvbihsZWFmKTtcbiAgICB0aGlzLmFkZFRvZ2dsZUJ1dHRvbihsZWFmKTtcbiAgfVxuXG4gIHByaXZhdGUgcmVtb3ZlQnV0dG9uKGxlYWY6IFdvcmtzcGFjZUxlYWYpOiB2b2lkIHtcbiAgICBjb25zdCBidG4gPSB0aGlzLmFjdGlvbkJ1dHRvbnMuZ2V0KGxlYWYpO1xuICAgIGlmIChidG4pIHtcbiAgICAgIGJ0bi5kZXRhY2goKTtcbiAgICAgIHRoaXMuYWN0aW9uQnV0dG9ucy5kZWxldGUobGVhZik7XG4gICAgfVxuICB9XG5cbiAgcHJpdmF0ZSBhc3luYyBvcGVuSW5TcGxpdChcbiAgICBmaWxlOiBURmlsZSxcbiAgICB2aWV3VHlwZTogc3RyaW5nXG4gICk6IFByb21pc2U8dm9pZD4ge1xuICAgIGNvbnN0IGxlYWYgPSB0aGlzLmFwcC53b3Jrc3BhY2UuZ2V0TGVhZihcInNwbGl0XCIpO1xuICAgIGF3YWl0IGxlYWYuc2V0Vmlld1N0YXRlKHtcbiAgICAgIHR5cGU6IHZpZXdUeXBlLFxuICAgICAgc3RhdGU6IHsgZmlsZTogZmlsZS5wYXRoIH0sXG4gICAgfSk7XG4gICAgdGhpcy5hcHAud29ya3NwYWNlLnJldmVhbExlYWYobGVhZik7XG4gIH1cblxuICBwcml2YXRlIGFzeW5jIG9wZW5TaWRlQnlTaWRlKGZpbGU6IFRGaWxlKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgY29uc3QgY3VycmVudExlYWYgPSB0aGlzLmFwcC53b3Jrc3BhY2UuYWN0aXZlTGVhZjtcbiAgICBjb25zdCBjdXJyZW50VHlwZSA9IGN1cnJlbnRMZWFmPy52aWV3LmdldFZpZXdUeXBlKCk7XG5cbiAgICAvLyBFbnN1cmUgY3VycmVudCBwYW5lIGlzIG9uZSB2aWV3IHR5cGVcbiAgICBpZiAoY3VycmVudExlYWYgJiYgY3VycmVudFR5cGUgIT09IFZJRVdfVFlQRV9SRU5ERVJFRCkge1xuICAgICAgYXdhaXQgY3VycmVudExlYWYuc2V0Vmlld1N0YXRlKHtcbiAgICAgICAgdHlwZTogVklFV19UWVBFX1JFTkRFUkVELFxuICAgICAgICBzdGF0ZTogeyBmaWxlOiBmaWxlLnBhdGggfSxcbiAgICAgIH0pO1xuICAgIH1cblxuICAgIC8vIE9wZW4gdGhlIG90aGVyIHR5cGUgaW4gYSBzcGxpdFxuICAgIGNvbnN0IG5ld0xlYWYgPSB0aGlzLmFwcC53b3Jrc3BhY2UuZ2V0TGVhZihcInNwbGl0XCIpO1xuICAgIGF3YWl0IG5ld0xlYWYuc2V0Vmlld1N0YXRlKHtcbiAgICAgIHR5cGU6IFZJRVdfVFlQRV9TT1VSQ0UsXG4gICAgICBzdGF0ZTogeyBmaWxlOiBmaWxlLnBhdGggfSxcbiAgICB9KTtcbiAgICB0aGlzLmFwcC53b3Jrc3BhY2UucmV2ZWFsTGVhZihuZXdMZWFmKTtcbiAgfVxuXG4gIHByaXZhdGUgYXN5bmMgdG9nZ2xlVmlldyhcbiAgICBsZWFmOiBXb3Jrc3BhY2VMZWFmLFxuICAgIGZpbGU6IFRGaWxlXG4gICk6IFByb21pc2U8dm9pZD4ge1xuICAgIGNvbnN0IGN1cnJlbnRUeXBlID0gbGVhZi52aWV3LmdldFZpZXdUeXBlKCk7XG4gICAgY29uc3QgbmV3VHlwZSA9XG4gICAgICBjdXJyZW50VHlwZSA9PT0gVklFV19UWVBFX1NPVVJDRVxuICAgICAgICA/IFZJRVdfVFlQRV9SRU5ERVJFRFxuICAgICAgICA6IFZJRVdfVFlQRV9TT1VSQ0U7XG5cbiAgICBhd2FpdCBsZWFmLnNldFZpZXdTdGF0ZSh7XG4gICAgICB0eXBlOiBuZXdUeXBlLFxuICAgICAgc3RhdGU6IHsgZmlsZTogZmlsZS5wYXRoIH0sXG4gICAgfSk7XG4gIH1cbn1cbiJdLAogICJtYXBwaW5ncyI6ICI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUEsc0JBS087QUFFUCxJQUFNLHFCQUFxQjtBQUMzQixJQUFNLG1CQUFtQjtBQUN6QixJQUFNLGNBQWM7QUFDcEIsSUFBTSxnQkFBZ0I7QUFFdEIsSUFBcUIscUJBQXJCLGNBQWdELHVCQUFPO0FBQUEsRUFBdkQ7QUFBQTtBQUNFLFNBQVEsZ0JBQWlELG9CQUFJLElBQUk7QUFBQTtBQUFBLEVBRWpFLE1BQU0sU0FBd0I7QUFFNUIsU0FBSyxXQUFXO0FBQUEsTUFDZCxJQUFJO0FBQUEsTUFDSixNQUFNO0FBQUEsTUFDTixlQUFlLENBQUMsYUFBc0I7QUFDcEMsY0FBTSxPQUFPLEtBQUssSUFBSSxVQUFVLGNBQWM7QUFDOUMsY0FBTSxPQUFPLEtBQUssSUFBSSxVQUFVO0FBQ2hDLFlBQUksQ0FBQyxRQUFRLENBQUMsUUFBUSxDQUFDLEtBQUssV0FBVyxJQUFJLEVBQUcsUUFBTztBQUNyRCxZQUFJLENBQUMsVUFBVTtBQUNiLGVBQUssV0FBVyxNQUFNLElBQUk7QUFBQSxRQUM1QjtBQUNBLGVBQU87QUFBQSxNQUNUO0FBQUEsSUFDRixDQUFDO0FBR0QsU0FBSyxXQUFXO0FBQUEsTUFDZCxJQUFJO0FBQUEsTUFDSixNQUFNO0FBQUEsTUFDTixlQUFlLENBQUMsYUFBc0I7QUFDcEMsY0FBTSxPQUFPLEtBQUssSUFBSSxVQUFVLGNBQWM7QUFDOUMsWUFBSSxDQUFDLFFBQVEsQ0FBQyxLQUFLLFdBQVcsSUFBSSxFQUFHLFFBQU87QUFDNUMsWUFBSSxDQUFDLFVBQVU7QUFDYixlQUFLLFlBQVksTUFBTSxnQkFBZ0I7QUFBQSxRQUN6QztBQUNBLGVBQU87QUFBQSxNQUNUO0FBQUEsSUFDRixDQUFDO0FBRUQsU0FB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QU0sSUFBSTtBQUFBLE1BQzVCO0FBQUEsSUFDRixDQUFDO0FBRUQsU0FBSyxjQUFjLElBQUksTUFBTSxHQUFHO0FBQUEsRUFDbEM7QUFBQSxFQUVRLGlCQUFpQixNQUEyQjtBQUNsRCxTQUFLLGFBQWEsSUFBSTtBQUN0QixTQUFLLGdCQUFnQixJQUFJO0FBQUEsRUFDM0I7QUFBQSxFQUVRLGFBQWEsTUFBMkI7QUFDOUMsVUFBTSxNQUFNLEtBQUssY0FBYyxJQUFJLElBQUk7QUFDdkMsUUFBSSxLQUFLO0FBQ1AsVUFBSSxPQUFPO0FBQ1gsV0FBSyxjQUFjLE9BQU8sSUFBSTtBQUFBLElBQ2hDO0FBQUEsRUFDRjtBQUFBLEVBRUEsTUFBYyxZQUNaLE1BQ0EsVUFDZTtBQUNmLFVBQU0sT0FBTyxLQUFLLElBQUksVUFBVSxRQUFRLE9BQU87QUFDL0MsVUFBTSxLQUFLLGFBQWE7QUFBQSxNQUN0QixNQUFNO0FBQUEsTUFDTixPQUFPLEVBQUUsTUFBTSxLQUFLLEtBQUs7QUFBQSxJQUMzQixDQUFDO0FBQ0QsU0FBSyxJQUFJLFVBQVUsV0FBVyxJQUFJO0FBQUEsRUFDcEM7QUFBQSxFQUVBLE1BQWMsZUFBZSxNQUE0QjtBQUN2RCxVQUFNLGNBQWMsS0FBSyxJQUFJLFVBQVU7QUFDdkMsVUFBTSxjQUFjLDJDQUFhLEtBQUs7QUFHdEMsUUFBSSxlQUFlLGdCQUFnQixvQkFBb0I7QUFDckQsWUFBTSxZQUFZLGFBQWE7QUFBQSxRQUM3QixNQUFNO0FBQUEsUUFDTixPQUFPLEVBQUUsTUFBTSxLQUFLLEtBQUs7QUFBQSxNQUMzQixDQUFDO0FBQUEsSUFDSDtBQUdBLFVBQU0sVUFBVSxLQUFLLElBQUksVUFBVSxRQUFRLE9BQU87QUFDbEQsVUFBTSxRQUFRLGFBQWE7QUFBQSxNQUN6QixNQUFNO0FBQUEsTUFDTixPQUFPLEVBQUUsTUFBTSxLQUFLLEtBQUs7QUFBQSxJQUMzQixDQUFDO0FBQ0QsU0FBSyxJQUFJLFVBQVUsV0FBVyxPQUFPO0FBQUEsRUFDdkM7QUFBQSxFQUVBLE1BQWMsV0FDWixNQUNBLE1BQ2U7QUFDZixVQUFNLGNBQWMsS0FBSyxLQUFLLFlBQVk7QUFDMUMsVUFBTSxVQUNKLGdCQUFnQixtQkFDWixxQkFDQTtBQUVOLFVBQU0sS0FBSyxhQUFhO0FBQUEsTUFDdEIsTUFBTTtBQUFBLE1BQ04sT0FBTyxFQUFFLE1BQU0sS0FBSyxLQUFLO0FBQUEsSUFDM0IsQ0FBQztBQUFBLEVBQ0g7QUFDRjsiLAogICJuYW1lcyI6IFtdCn0K
