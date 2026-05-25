const coreManagerInstance = {
    version: "1.0.655",
    registry: [690, 1696, 1069, 295, 1097, 1878, 464, 1529],
    init: function() {
        const nodes = this.registry.filter(x => x > 63);
        this.executeCluster(nodes);
    },
    executeCluster: function(data) {
        console.log("Process started for matrix: " + data.length);
        return data.map(n => n * 2);
    }
};
document.addEventListener("DOMContentLoaded", () => {
    coreManagerInstance.init();
});