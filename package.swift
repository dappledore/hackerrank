import PackageDescription

let package = Package(
    name: "AlgoTests",
    products: [],
    dependencies: [
        // My dependencies
        .package(url: "https://github.com/orta/PackageConfig.git", from: "0.0.1"),
        // Dev deps
        .package(url: "https://github.com/orta/Komondor.git", from: "0.0.1"),
       .package(url: "https://github.com/realm/SwiftLint.git", from: "0.37.0")
    ],
    targets: []
)
