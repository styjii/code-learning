# ✅ Corrigés : exercices TypeScript

> Corrigés des **27 exercices** et des **3 mini-projets** du document `typescript.md`. Le code a été **vérifié avec `tsc` en mode `strict`** (configuration de la section 0 de l'énoncé, TypeScript 5.x) et, quand c'était possible, **exécuté** avec `tsx`.
>
> 💡 Les lignes `// @ts-expect-error` montrent volontairement une **erreur de type attendue** : le compilateur doit la signaler. Si vous la retirez, `tsc` refusera de compiler.
>
> ℹ️ Les exercices qui dépendent d'un service externe ou d'un gros framework (Angular, Vue, NestJS, bases de données) sont donnés **à titre de modèle** : ils ne peuvent pas être exécutés sans leur environnement.

## 📑 Sommaire

[Partie 1](#partie-1--fondamentaux) · [Partie 2](#partie-2--poo-et-génériques) · [Partie 3](#partie-3--types-avancés) · [Partie 4 (projets)](#partie-4--mini-projets) · [Partie 5](#partie-5--asynchrone) · [Partie 6](#partie-6--modules-déclarations-configuration) · [Partie 7](#partie-7--décorateurs) · [Partie 8](#partie-8--web-et-frameworks) · [Partie 9](#partie-9--données-et-tests)

---

# Partie 1 : fondamentaux

## Exercice 1 : variables typées

```ts
// fichier: src/ex01.ts
const userName = "Alice"; // inféré : string
const userAge = 30; // inféré : number
const isAdmin = false; // inféré : boolean
const hobbies: string[] = ["lecture", "code", "échecs"]; // annotation utile : tableau
const locat: [string, number] = ["Paris", 75001]; // tuple : ville et code postal

console.log(userName, userAge, isAdmin, hobbies, locat);
```

> Avec `const` et une valeur littérale, le compilateur **infère** déjà le type : n'écrivez `: string` que quand cela apporte quelque chose.

## Exercice 2 : fonctions typées

```ts
// fichier: src/ex02.ts
function sum(a: number, b: number): number {
    return a + b;
}

function multiply(a: number, b: number): number {
    return a * b;
}

function greetUser(name: string): string {
    return `Bonjour, ${name} !`;
}

function sayHello(name: string, age?: number): string {
    // `age` vaut `number | undefined` : il faut tester avant de l'utiliser
    return age === undefined
        ? `Bonjour ${name}`
        : `Bonjour ${name}, vous avez ${age} ans`;
}

// Alias de type de fonction
type CalcFn = (a: number, b: number) => number;

const add: CalcFn = (a, b) => a + b; // les paramètres sont inférés depuis CalcFn
const mult: CalcFn = (a, b) => a * b;

// ➕ Paramètre rest et valeur par défaut
function total(...nombres: number[]): number {
    return nombres.reduce((somme, n) => somme + n, 0);
}

function puissance(base: number, exposant = 2): number {
    return base ** exposant;
}

console.log(sum(2, 3), multiply(4, 5), greetUser("Alice")); // 5 20 "Bonjour, Alice !"
console.log(sayHello("Bob"), "|", sayHello("Bob", 30));
console.log(add(1, 2), mult(3, 4), total(1, 2, 3, 4), puissance(5), puissance(2, 10)); // 3 12 10 25 1024
```

## Exercice 3 : tableaux et tuples

```ts
// fichier: src/ex03.ts
const couleurs: string[] = ["rouge", "vert"];
couleurs.push("bleu");

const premiers: readonly number[] = [2, 3, 5, 7, 11];
// @ts-expect-error : « Property 'push' does not exist on type 'readonly number[]' »
premiers.push(13);

// Tuple étiqueté (les étiquettes documentent chaque position)
type Person = [name: string, age: number];
const alice: Person = ["Alice", 30];

console.log(couleurs, premiers.length, alice);
console.log(`${alice[0]} a ${alice[1]} ans`);
```

## Exercice 4 : énumérations

```ts
// fichier: src/ex04.ts
enum Status {
    Active,
    Inactive,
    Blocked,
}

function logStatus(status: Status): void {
    // Un enum numérique permet la correspondance inverse : Status[2] === "Blocked"
    console.log(`${Status[status]} (${status})`);
}

enum Direction {
    North = "N",
    South = "S",
    East = "E",
    West = "W",
}

function move(dir: Direction): string {
    switch (dir) {
        case Direction.North:
            return "Vous allez vers le nord";
        case Direction.South:
            return "Vous allez vers le sud";
        case Direction.East:
            return "Vous allez vers l'est";
        case Direction.West:
            return "Vous allez vers l'ouest";
    }
}

const enum LogLevel {
    Debug,
    Info,
    Error,
}

// ➕ Alternative moderne : objet `as const` + type déduit
const Dir = { North: "N", South: "S", East: "E", West: "W" } as const;
type Dir = (typeof Dir)[keyof typeof Dir]; // "N" | "S" | "E" | "W"

function moveDir(dir: Dir): string {
    return `Cap : ${dir}`;
}

logStatus(Status.Blocked); // Blocked (2)
console.log(move(Direction.East), LogLevel.Info, moveDir(Dir.North));
```

> ✅ **Lequel choisir ?** Pour du code neuf, l'union de littéraux ou l'objet `as const` : aucune syntaxe spéciale à l'exécution (compatible avec `erasableSyntaxOnly` et l'exécution directe par Node.js), et les valeurs restent lisibles dans les journaux. Le `const enum` pose problème avec `isolatedModules` et les bundlers.

## Exercice 5 : interfaces et objets

```ts
// fichier: src/ex05.ts
interface User {
    name: string;
    age: number;
    isAdmin: boolean;
    hobbies?: string[]; // bonus : optionnel, pour ne pas casser les anciens objets
}

const user: User = { name: "Alice", age: 30, isAdmin: true, hobbies: ["lecture", "code"] };

function printUserInfo(user: User): void {
    const admin = user.isAdmin ? "oui" : "non";
    let ligne = `Nom : ${user.name}, Âge : ${user.age}, Admin : ${admin}`;
    if (user.hobbies && user.hobbies.length > 0) {
        ligne += `, Loisirs : ${user.hobbies.join(", ")}`;
    }
    console.log(ligne);
}

printUserInfo(user); // Nom : Alice, Âge : 30, Admin : oui, Loisirs : lecture, code
```

## Exercice 6 : héritage d'interfaces et classes

```ts
// fichier: src/ex06.ts
interface Book {
    title: string;
    author: string;
    year?: number;
}

function printBook(book: Book): void {
    const annee = book.year !== undefined ? ` (${book.year})` : "";
    console.log(`${book.title}, de ${book.author}${annee}`);
}

interface EBook extends Book {
    fileSize: number; // en Mo
}

class EBookReader {
    constructor(private readonly ebook: EBook) {}

    printDetails(): void {
        printBook(this.ebook);
        console.log(`Taille du fichier : ${this.ebook.fileSize} Mo`);
    }
}

printBook({ title: "Le Petit Prince", author: "Saint-Exupéry", year: 1943 });
new EBookReader({ title: "Dune", author: "Herbert", fileSize: 2.4 }).printDetails();
```

## Exercice 7 : alias, unions et littéraux

```ts
// fichier: src/ex07.ts
type ID = number | string;
const userId: ID = "user_abc";

function displayId(id: ID): void {
    if (typeof id === "number") {
        console.log(`ID numérique : ${id}`); // ici id : number
    } else {
        console.log(`ID texte : ${id}`); // ici id : string
    }
}

type UserRole = "admin" | "user" | "guest";

type User = {
    id: number;
    name: string;
    role: UserRole;
};

function describeUser(user: User): string {
    return `#${user.id} ${user.name} (${user.role})`;
}

displayId(42);
displayId(userId);
console.log(describeUser({ id: 1, name: "Alice", role: "admin" }));
// @ts-expect-error : "root" n'appartient pas à UserRole
describeUser({ id: 2, name: "Bob", role: "root" });
```

## Exercice 8 : unions discriminées

```ts
// fichier: src/ex08.ts
interface Admin {
    role: "admin";
    name: string;
    permissions: string[];
}

interface Guest {
    role: "guest";
    name: string;
    expiration: Date;
}

// ➕ Un troisième rôle
interface Moderator {
    role: "moderator";
    name: string;
    forums: string[];
}

type UserType = Admin | Guest | Moderator;

function assertNever(x: never): never {
    throw new Error(`Cas non géré : ${JSON.stringify(x)}`);
}

function handleUser(user: UserType): void {
    switch (user.role) {
        case "admin":
            console.log(`L'administrateur ${user.name} a les permissions : ${user.permissions.join(", ")}`);
            break;
        case "guest":
            console.log(`L'invité ${user.name} expire le : ${user.expiration.toLocaleDateString("fr-FR")}`);
            break;
        case "moderator":
            console.log(`Le modérateur ${user.name} gère : ${user.forums.join(", ")}`);
            break;
        default:
            // Si on oublie un rôle dans le `switch`, `user` n'est plus `never` : erreur de compilation
            assertNever(user);
    }
}

handleUser({ role: "admin", name: "Alice", permissions: ["lire", "écrire"] });
handleUser({ role: "guest", name: "Bob", expiration: new Date("2030-01-01") });
handleUser({ role: "moderator", name: "Chloé", forums: ["général"] });
```

## Exercice 9 : surcharge de fonctions

```ts
// fichier: src/ex09.ts
// Signatures publiques (surcharges)
function combine(a: number, b: number): number;
function combine(a: string, b: string): string;
function combine(a: number, b: string): string;
// Implémentation (invisible de l'extérieur) : doit être compatible avec toutes les surcharges
function combine(a: number | string, b: number | string): number | string {
    if (typeof a === "number" && typeof b === "number") {
        return a + b;
    }
    return `${a}${b}`;
}

console.log(combine(2, 3)); // 5
console.log(combine("foo", "bar")); // "foobar"
console.log(combine(10, "px")); // "10px"
// @ts-expect-error : aucune surcharge ne prend (string, number)
combine("px", 10);
```

---

# Partie 2 : POO et génériques

## Exercice 10 : classes, héritage et interfaces

```ts
// fichier: src/ex10.ts
interface Payable {
    getPay(): number;
}

abstract class Employee implements Payable {
    // Propriétés de paramètre : déclarent ET initialisent les attributs
    constructor(
        public readonly name: string,
        protected salary: number,
    ) {}

    describe(): string {
        return `${this.name} gagne ${this.salary} €`;
    }

    getPay(): number {
        return this.salary;
    }
}

class Developer extends Employee {}

class Manager extends Employee {
    constructor(
        name: string,
        salary: number,
        private readonly department: string,
    ) {
        super(name, salary);
    }

    override describe(): string {
        return `${super.describe()} et dirige le département ${this.department}`;
    }

    override getPay(): number {
        return this.salary * 1.2; // prime de 20 %
    }
}

const equipe: Employee[] = [new Developer("Alice", 3000), new Manager("Bob", 4000, "R&D")];
for (const e of equipe) {
    console.log(e.describe(), "→", e.getPay());
}
// @ts-expect-error : la classe est abstraite
new Employee("X", 1);
// @ts-expect-error : `salary` est protégé
console.log(equipe[0]?.salary);
```

## Exercice 11 : génériques

```ts
// fichier: src/ex11.ts
function reverseArray<T>(items: T[]): T[] {
    return [...items].reverse(); // copie : on ne modifie pas l'argument
}

interface ApiResponse<T> {
    data: T;
    error?: string;
}

class DataStore<T extends { id: number }> {
    private items: T[] = [];

    add(item: T): void {
        this.items.push(item);
    }

    getAll(): T[] {
        return [...this.items];
    }

    findById(id: number): T | undefined {
        return this.items.find((item) => item.id === id);
    }
}

const nombres = reverseArray([1, 2, 3]); // number[]
const lettres = reverseArray(["a", "b"]); // string[]
const reponse: ApiResponse<string[]> = { data: lettres };

const store = new DataStore<{ id: number; nom: string }>();
store.add({ id: 1, nom: "Alice" });
console.log(nombres, reponse, store.getAll(), store.findById(1), store.findById(9));
// @ts-expect-error : un objet sans `id` ne respecte pas la contrainte
new DataStore<{ nom: string }>();
```

## Exercice 12 : accès typé aux clés (`keyof`)

```ts
// fichier: src/ex12.ts
interface Config {
    theme: "light" | "dark";
    lang: string;
    debug: boolean;
}

const config: Config = { theme: "dark", lang: "fr", debug: true };

// K est l'une des clés de Config ; le type de retour dépend de K
function getConfigValue<K extends keyof Config>(key: K): Config[K] {
    return config[key];
}

const debug = getConfigValue("debug"); // boolean
const theme = getConfigValue("theme"); // "light" | "dark"
const verifie: boolean = debug;
console.log(verifie, theme);
// @ts-expect-error : « couleur » n'est pas une clé de Config
getConfigValue("couleur");
```

## Exercice 13 : mixins et composition

```ts
// fichier: src/ex13.ts
import { randomUUID } from "node:crypto";

// Un constructeur quelconque (nécessaire pour typer les mixins)
type Constructor<T = object> = new (...args: any[]) => T;

// Mixin 1 : journalisation
function Logger<TBase extends Constructor>(Base: TBase) {
    return class extends Base {
        log(message: string): void {
            console.log(`[${this.constructor.name}] ${message}`);
        }
    };
}

// Mixin 2 : numéro de série
function Serial<TBase extends Constructor>(Base: TBase) {
    return class extends Base {
        readonly serialNumber: string = randomUUID().slice(0, 8);
    };
}

// Composition : un objet « interrupteur » détenu par le robot
class Power {
    private on = false;
    turnOn(): void {
        this.on = true;
    }
    turnOff(): void {
        this.on = false;
    }
    get isOn(): boolean {
        return this.on;
    }
}

class BaseRobot {
    constructor(public readonly name: string) {}
}

class Robot extends Logger(Serial(BaseRobot)) {
    private readonly power = new Power();

    powerOn(): void {
        this.power.turnOn();
        this.log(`${this.name} allumé (série ${this.serialNumber})`);
    }

    powerOff(): void {
        this.power.turnOff();
        this.log(`${this.name} éteint`);
    }

    get isOn(): boolean {
        return this.power.isOn;
    }
}

const robot = new Robot("R2");
robot.powerOn();
console.log(robot.isOn); // true
robot.powerOff();
```

> 💡 **Composition ou héritage ?** Préférez la composition quand la relation est « a un » (un robot *a une* alimentation) : elle est plus flexible, car on peut remplacer l'objet composé sans changer la hiérarchie de classes.

---

# Partie 3 : types avancés

## Exercice 14 : types utilitaires

```ts
// fichier: src/ex14.ts
interface Product {
    id: number;
    name: string;
    price: number;
    stock: number;
}

// 1. Partial : tous les champs deviennent optionnels (on retire `id` : non modifiable)
type ProductUpdate = Partial<Omit<Product, "id">>;

function updateProduct(product: Product, changes: ProductUpdate): Product {
    return { ...product, ...changes };
}

// 2. Pick : on ne garde que certaines clés
interface UserFull {
    id: number;
    name: string;
    email: string;
    password: string;
}
type UserPreview = Pick<UserFull, "id" | "name">;
const apercu: UserPreview = { id: 1, name: "Alice" };

// 3. ➕ Omit, Required, Readonly
type PublicUser = Omit<UserFull, "password">;
type ProductComplet = Required<ProductUpdate>;
type ProductFige = Readonly<Product>;

// 4. Record
type Day = "lundi" | "mardi" | "mercredi" | "jeudi" | "vendredi";
const planning: Record<Day, string[]> = {
    lundi: ["maths"],
    mardi: [],
    mercredi: ["sport"],
    jeudi: [],
    vendredi: ["projet"],
};

// 5. DeepReadonly : rend immuable récursivement
type DeepReadonly<T> = T extends (...args: never[]) => unknown
    ? T
    : T extends readonly (infer U)[]
      ? readonly DeepReadonly<U>[]
      : T extends object
        ? { readonly [K in keyof T]: DeepReadonly<T[K]> }
        : T;

interface Reglages {
    theme: { couleur: string; tailles: number[] };
}
const reglages: DeepReadonly<Reglages> = { theme: { couleur: "bleu", tailles: [1, 2] } };
// @ts-expect-error : propriété en lecture seule, même en profondeur
reglages.theme.couleur = "rouge";
// @ts-expect-error : le tableau est lui aussi en lecture seule
reglages.theme.tailles.push(3);

// 6. ➕ ReturnType et Awaited
function creerUtilisateur() {
    return { id: 1, nom: "Alice" };
}
type Utilisateur = ReturnType<typeof creerUtilisateur>; // { id: number; nom: string }
type Texte = Awaited<Promise<string>>; // string

const maj = updateProduct({ id: 1, name: "Stylo", price: 2, stock: 10 }, { price: 3 });
const figee: ProductFige = maj;
const complet: ProductComplet = { name: "x", price: 1, stock: 1 };
const u: Utilisateur = creerUtilisateur();
const t: Texte = "ok";
const pub: PublicUser = { id: 1, name: "A", email: "a@b.c" };
console.log(maj, apercu, planning.lundi, figee.name, complet.name, u.nom, t, pub.email);
```

## Exercice 15 : types mappés et conditionnels

```ts
// fichier: src/ex15.ts
type Car = { make: string; model: string; year: number };

// 2. Mappé « à la main » : toutes les clés sauf `year`, plus `year` optionnel
type CarWithOptionalYear = {
    [K in Exclude<keyof Car, "year">]: Car[K];
} & { year?: Car["year"] };

// 3. Pick
type CarInfo = Pick<Car, "make" | "model">;

// 4. Conditionnel
type IsCar<T> = T extends Car ? true : false;

// 5. ➕ Nullable
type Nullable<T> = { [K in keyof T]: T[K] | null };

const sansAnnee: CarWithOptionalYear = { make: "Renault", model: "Clio" };
const info: CarInfo = { make: "Peugeot", model: "208" };
const test1: IsCar<Car> = true;
const test2: IsCar<string> = false;
const test3: IsCar<{ make: string }> = false; // il manque `model` et `year`
const nul: Nullable<Car> = { make: "Fiat", model: null, year: null };
console.log(sansAnnee, info, test1, test2, test3, nul);
```

## Exercice 16 : `unknown`, gardes de type et `never`

```ts
// fichier: src/ex16.ts
interface User {
    name: string;
    age: number;
}

function parseJson(texte: string): unknown {
    return JSON.parse(texte);
}

// Garde de type : renvoie un booléen ET informe le compilateur
function isUser(valeur: unknown): valeur is User {
    return (
        typeof valeur === "object" &&
        valeur !== null &&
        "name" in valeur &&
        typeof valeur.name === "string" &&
        "age" in valeur &&
        typeof valeur.age === "number"
    );
}

const donnees = parseJson('{"name":"Alice","age":30}');
if (isUser(donnees)) {
    console.log(donnees.name.toUpperCase()); // ici donnees : User
} else {
    console.log("Format inattendu");
}

// Capture d'erreur : `e` est `unknown`
try {
    parseJson("{pas du json");
} catch (e: unknown) {
    if (e instanceof Error) {
        console.log("Erreur :", e.message);
    }
}

// Comparaison any / unknown
const a: any = "texte";
a.fonctionInexistante; // `any` désactive toute vérification : aucune erreur (dangereux)

const u: unknown = "texte";
// @ts-expect-error : on ne peut rien faire d'un `unknown` sans le vérifier
u.toUpperCase();
if (typeof u === "string") {
    u.toUpperCase(); // OK après vérification
}
```

## Exercice 17 : `as const`, `satisfies` et types gabarits

```ts
// fichier: src/ex17.ts
// 1. as const : les valeurs deviennent des littéraux en lecture seule
const routes = { home: "/", about: "/a-propos", contact: "/contact" } as const;
type Route = (typeof routes)[keyof typeof routes]; // "/" | "/a-propos" | "/contact"
const r: Route = "/contact";

// 2. satisfies : vérifie la forme SANS élargir le type inféré
const couleurs = {
    rouge: [255, 0, 0],
    vert: "#00ff00",
} satisfies Record<string, string | number[]>;

couleurs.rouge.map((x) => x * 2); // OK : TypeScript sait que `rouge` est un number[]

const annote: Record<string, string | number[]> = { rouge: [255, 0, 0] };
// @ts-expect-error : avec l'annotation, `rouge` est `string | number[]` : `map` n'existe pas sur string
annote.rouge.map((x) => x);

// 3. Type gabarit
type EventName = "click" | "focus";
type Handler = `on${Capitalize<EventName>}`; // "onClick" | "onFocus"
const h: Handler = "onClick";
// @ts-expect-error
const h2: Handler = "onHover";

console.log(r, couleurs.vert, h, h2);
```

> 💡 **Pourquoi `satisfies` ?** Une annotation (`: Type`) *remplace* le type inféré par un type plus large. `satisfies` *contrôle* que la valeur respecte le type tout en **conservant** le type précis.

---

# Partie 4 : mini-projets

## Projet A : journal d'événements

```ts
// fichier: src/projetA.ts
// A1 : tuples
type EventTuple = [eventName: string, payload: Record<string, unknown>];

const eventLog: EventTuple[] = [
    ["login", { user: "alice", time: "12:00" }],
    ["purchase", { user: "bob", item: "livre", price: 25 }],
    ["logout", { user: "alice", time: "12:30", metadata: { raison: "inactivité" } }],
];

// A2 + A4 : union discriminée, avec `metadata` optionnelle
interface Base {
    user: string;
    metadata?: Record<string, unknown>;
}
interface LoginEvent extends Base {
    type: "login";
    time: string;
}
interface LogoutEvent extends Base {
    type: "logout";
    time: string;
}
interface PurchaseEvent extends Base {
    type: "purchase";
    item: string;
    price: number;
}
type AppEvent = LoginEvent | LogoutEvent | PurchaseEvent;

function decrire(event: AppEvent): string {
    switch (event.type) {
        case "login":
            return `Utilisateur ${event.user} connecté à ${event.time}`;
        case "logout":
            return `Utilisateur ${event.user} déconnecté à ${event.time}`;
        case "purchase":
            return `${event.user} a acheté ${event.item} pour ${event.price} $`;
    }
}

function handleEvent(event: AppEvent): void {
    let message = decrire(event);
    if (event.metadata) {
        message += ` 📎 Métadonnées : ${JSON.stringify(event.metadata)}`;
    }
    console.log(message);
}

// A3 : conversion avec validation (le payload est `unknown` : on vérifie chaque champ)
function lireTexte(payload: Record<string, unknown>, cle: string): string {
    const valeur = payload[cle];
    if (typeof valeur !== "string") throw new Error(`Champ « ${cle} » manquant ou invalide`);
    return valeur;
}

function lireNombre(payload: Record<string, unknown>, cle: string): number {
    const valeur = payload[cle];
    if (typeof valeur !== "number") throw new Error(`Champ « ${cle} » manquant ou invalide`);
    return valeur;
}

function lireMetadata(payload: Record<string, unknown>): Pick<Base, "metadata"> {
    const m = payload["metadata"];
    return typeof m === "object" && m !== null ? { metadata: m as Record<string, unknown> } : {};
}

function convertToAppEvent([name, payload]: EventTuple): AppEvent {
    const user = lireTexte(payload, "user");
    const metadata = lireMetadata(payload);
    switch (name) {
        case "login":
            return { type: "login", user, time: lireTexte(payload, "time"), ...metadata };
        case "logout":
            return { type: "logout", user, time: lireTexte(payload, "time"), ...metadata };
        case "purchase":
            return {
                type: "purchase",
                user,
                item: lireTexte(payload, "item"),
                price: lireNombre(payload, "price"),
                ...metadata,
            };
        default:
            throw new Error(`Événement inconnu : ${name}`);
    }
}

for (const event of eventLog) {
    handleEvent(convertToAppEvent(event));
}
// Utilisateur alice connecté à 12:00
// bob a acheté livre pour 25 $
// Utilisateur alice déconnecté à 12:30 📎 Métadonnées : {"raison":"inactivité"}
```

## Projet B : gestionnaire de paramètres

```ts
// fichier: src/projetB.ts
interface UserSettings {
    theme: "light" | "dark";
    notifications: boolean;
    fontSize: "small" | "medium" | "large";
}

// B1
const defaultSettings: UserSettings = {
    theme: "light",
    notifications: true,
    fontSize: "medium",
};

// B2 : `??` règle le piège de `{ ...defaults, ...user }` quand une valeur vaut `undefined`
function mergeSettings(userSettings: Partial<UserSettings>): UserSettings {
    return {
        theme: userSettings.theme ?? defaultSettings.theme,
        notifications: userSettings.notifications ?? defaultSettings.notifications,
        fontSize: userSettings.fontSize ?? defaultSettings.fontSize,
    };
}

// B3 : vérification manuelle de chaque clé (les données réelles peuvent venir de JSON)
const THEMES: readonly string[] = ["light", "dark"];
const TAILLES: readonly string[] = ["small", "medium", "large"];

function validateSettings(settings: Partial<UserSettings>): string[] {
    const erreurs: string[] = [];
    if (settings.theme !== undefined && !THEMES.includes(settings.theme)) {
        erreurs.push(`Thème invalide : ${settings.theme}`);
    }
    if (settings.notifications !== undefined && typeof settings.notifications !== "boolean") {
        erreurs.push(`Notifications invalides : ${String(settings.notifications)}`);
    }
    if (settings.fontSize !== undefined && !TAILLES.includes(settings.fontSize)) {
        erreurs.push(`Taille de police invalide : ${settings.fontSize}`);
    }
    return erreurs;
}

// B4
function getSetting<K extends keyof UserSettings>(key: K, settings: UserSettings): UserSettings[K] {
    return settings[key];
}

// B5
type SettingsMeta = {
    [K in keyof UserSettings]: { label: string; description: string };
};

const settingsInfo: SettingsMeta = {
    theme: { label: "Thème", description: "Apparence claire ou sombre" },
    notifications: { label: "Notifications", description: "Activer les alertes" },
    fontSize: { label: "Police", description: "Taille du texte" },
};

const merged = mergeSettings({ theme: "dark" });
console.log(merged); // { theme: 'dark', notifications: true, fontSize: 'medium' }
console.log(validateSettings({ theme: "blue" as never, fontSize: "huge" as never }));
// [ 'Thème invalide : blue', 'Taille de police invalide : huge' ]
const theme: "light" | "dark" = getSetting("theme", merged);
console.log(theme, settingsInfo.theme.label);
```

## Projet C : calculatrice typée

```ts
// fichier: src/projetC.ts
// C1
type Operator = "add" | "subtract" | "multiply" | "divide";
type Expression = [Operator, number, number];

// C2
class DivisionParZeroError extends Error {
    constructor() {
        super("Division par zéro");
        this.name = "DivisionParZeroError";
    }
}

function evaluate([op, a, b]: Expression): number {
    switch (op) {
        case "add":
            return a + b;
        case "subtract":
            return a - b;
        case "multiply":
            return a * b;
        case "divide":
            if (b === 0) throw new DivisionParZeroError();
            return a / b;
        default: {
            const _exhaustif: never = op; // erreur de compilation si on oublie un opérateur
            throw new Error(`Opérateur inconnu : ${String(_exhaustif)}`);
        }
    }
}

// C3
const history: Expression[] = [
    ["add", 4, 2],
    ["multiply", 3, 5],
    ["divide", 9, 3],
];

function printHistory(): void {
    for (const [op, a, b] of history) {
        console.log(`${op}(${a}, ${b}) = ${evaluate([op, a, b])}`);
    }
}

// C4
type Result<T extends Expression> = {
    expression: T;
    result: number;
};

function evaluateWithResult<T extends Expression>(expr: T): Result<T> {
    return { expression: expr, result: evaluate(expr) };
}

console.log(evaluate(["add", 4, 2])); // 6
printHistory();
// add(4, 2) = 6
// multiply(3, 5) = 15
// divide(9, 3) = 3
console.log(evaluateWithResult(["subtract", 10, 4])); // { expression: [ 'subtract', 10, 4 ], result: 6 }
try {
    evaluate(["divide", 1, 0]);
} catch (e: unknown) {
    console.log(e instanceof DivisionParZeroError ? "Division par zéro interceptée" : "autre erreur");
}
```

---

# Partie 5 : asynchrone

## Exercice 18 : promesses et `async` / `await`

```ts
// fichier: src/ex18.ts
interface Options {
    delai?: number;
    echec?: boolean;
}

// 1. Une promesse qui se résout (ou se rejette) après un délai
function fetchData({ delai = 2000, echec = false }: Options = {}): Promise<string> {
    return new Promise((resolve, reject) => {
        setTimeout(() => (echec ? reject(new Error("Échec réseau")) : resolve("données")), delai);
    });
}

// 2 + 3. async/await avec gestion d'erreur
async function getData(options?: Options): Promise<void> {
    try {
        const donnees = await fetchData(options);
        console.log("Reçu :", donnees);
    } catch (e: unknown) {
        console.error("Erreur :", e instanceof Error ? e.message : e);
    }
}

// 4. Promise.all : en parallèle, donc ~300 ms au total et non 900 ms
async function toutEnParallele(): Promise<void> {
    const debut = Date.now();
    const resultats = await Promise.all([
        fetchData({ delai: 300 }),
        fetchData({ delai: 300 }),
        fetchData({ delai: 300 }),
    ]);
    console.log(resultats, `${Date.now() - debut} ms`);
}

// 5. allSettled : attend tout, sans jamais échouer ; all : échoue dès la première erreur
async function comparer(): Promise<void> {
    const reglees = await Promise.allSettled([
        fetchData({ delai: 100 }),
        fetchData({ delai: 100, echec: true }),
    ]);
    console.log(reglees.map((r) => r.status)); // [ 'fulfilled', 'rejected' ]

    const premiere = await Promise.race([fetchData({ delai: 50 }), fetchData({ delai: 500 })]);
    console.log("race :", premiere);
}

// 6. Délai maximal
function avecDelaiMax<T>(promesse: Promise<T>, ms: number): Promise<T> {
    let minuteur: NodeJS.Timeout;
    const expiration = new Promise<never>((_, reject) => {
        minuteur = setTimeout(() => reject(new Error(`Délai de ${ms} ms dépassé`)), ms);
    });
    return Promise.race([promesse, expiration]).finally(() => clearTimeout(minuteur));
}

async function main(): Promise<void> {
    await getData({ delai: 200 });
    await getData({ delai: 200, echec: true });
    await toutEnParallele();
    await comparer();
    try {
        await avecDelaiMax(fetchData({ delai: 1000 }), 100);
    } catch (e: unknown) {
        console.error(e instanceof Error ? e.message : e);
    }
}

await main();
```

> 💡 Avec `fetch`, la méthode la plus simple pour un délai maximal est `fetch(url, { signal: AbortSignal.timeout(1000) })` : la requête est réellement **annulée**, au lieu d'être seulement ignorée.

---

# Partie 6 : modules, déclarations, configuration

## Exercice 19 : modules et espaces de noms

```ts
// fichier: src/math.ts
export function add(a: number, b: number): number {
    return a + b;
}
export function subtract(a: number, b: number): number {
    return a - b;
}
export function multiply(a: number, b: number): number {
    return a * b;
}
```

```ts
// fichier: src/geometry-namespace.ts
// Espace de noms (style historique)
export namespace Geometry {
    export function circleArea(r: number): number {
        return Math.PI * r ** 2;
    }
    export function rectangleArea(largeur: number, hauteur: number): number {
        return largeur * hauteur;
    }
}
```

```ts
// fichier: src/geometry.ts
// ➕ Même chose sans `namespace` : un simple module ES
export function circleArea(r: number): number {
    return Math.PI * r ** 2;
}
export function rectangleArea(largeur: number, hauteur: number): number {
    return largeur * hauteur;
}
```

```ts
// fichier: src/app19.ts
import { add, multiply, subtract } from "./math.js"; // ← extension .js avec NodeNext
import { Geometry } from "./geometry-namespace.js";
import * as Geo from "./geometry.js";

console.log(add(2, 3), subtract(5, 1), multiply(4, 4)); // 5 4 16
console.log(Geometry.circleArea(1).toFixed(2), Geometry.rectangleArea(3, 4)); // 3.14 12
console.log(Geo.circleArea(1).toFixed(2), Geo.rectangleArea(3, 4)); // identique
```

> ⚠️ Un `namespace` produit du code JavaScript à l'exécution : il est refusé par `erasableSyntaxOnly`. Un module ES (`import * as Geo`) donne le même regroupement, sans syntaxe spéciale.

## Exercice 20 : fichiers de déclaration (`.d.ts`)

**1. Paquet `@types`**

```bash
npm install lodash
npm install --save-dev @types/lodash
```

```ts
// fichier: src/ex20-lodash.ts
import _ from "lodash";

const groupes = _.groupBy(["un", "deux", "trois"], (mot) => mot.length);
console.log(groupes); // { '2': [ 'un' ], '4': [ 'deux' ], '5': [ 'trois' ] }
const n: number = _.sum([1, 2, 3]); // les types viennent de @types/lodash
console.log(n);
```

> ℹ️ `axios` n'a pas besoin de paquet `@types` : il **embarque ses propres types**. Vérifiez la clé `types` de son `package.json`.

**2 et 4. Déclaration d'un module sans types (ou inventé)**

```ts
// fichier: src/types/ma-lib.d.ts
// @norun
declare module "ma-lib-inventee" {
    export function saluer(nom: string): string;
    export const VERSION: string;
}

// Pour une bibliothèque JS existante dont on ne veut pas détailler les types :
declare module "vieille-lib-sans-types";
```

```ts
// fichier: src/ex20-usage.ts
// @norun
import { saluer, VERSION } from "ma-lib-inventee";

console.log(saluer("Alice"), VERSION); // typé grâce au fichier .d.ts
```

**3. Déclarations ambiantes (variable globale)**

```ts
// fichier: src/types/globals.d.ts
// @norun
declare const APP_VERSION: string; // définie à la compilation par un bundler ou un script

// Pour enrichir un type global existant :
interface Window {
    appVersion?: string;
}
```

```ts
// fichier: src/ex20-global.ts
// @norun
console.log(`Version : ${APP_VERSION}`);
```

> 💡 `declare` ne crée **rien** à l'exécution : il promet seulement au compilateur que la valeur existe. Définissez-la réellement (option `define` d'esbuild/Vite, par exemple).

## Exercice 21 : structure du projet et alias

`tsconfig.json` :

```json
{
    "compilerOptions": {
        "target": "ES2022",
        "module": "NodeNext",
        "moduleResolution": "NodeNext",
        "rootDir": "src",
        "outDir": "build",
        "strict": true,
        "baseUrl": ".",
        "paths": {
            "@services/*": ["src/services/*"]
        }
    },
    "include": ["src"]
}
```

⚠️ `paths` ne sert **qu'au compilateur** : le JavaScript produit contiendrait toujours `@services/...`, que Node.js ne sait pas résoudre. Trois solutions :

1. **Imports de sous-chemins natifs de Node.js** (sans outil supplémentaire), dans `package.json` :

   ```json
   {
       "type": "module",
       "imports": {
           "#services/*": "./build/services/*"
       }
   }
   ```

   ```ts
   import { listerUtilisateurs } from "#services/utilisateurs.js";
   ```

   Côté `tsconfig.json`, TypeScript comprend aussi ces `imports` avec `moduleResolution: NodeNext`.

2. **`tsc-alias`** : après `tsc`, un outil réécrit les alias dans le JS produit (`npx tsc && npx tsc-alias`).
3. **Un bundler** (Vite, esbuild, tsup) qui résout les alias lui-même.

---

# Partie 7 : décorateurs

## Exercice 22 : décorateurs

**Partie A : décorateurs standard (TypeScript 5+, aucune option à activer)**

```ts
// fichier: src/ex22.ts
// 2. Décorateur de méthode : mesure la durée
function logExecutionTime<This, Args extends unknown[], Return>(
    target: (this: This, ...args: Args) => Return,
    context: ClassMethodDecoratorContext<This, (this: This, ...args: Args) => Return>,
) {
    const nom = String(context.name);
    return function (this: This, ...args: Args): Return {
        const debut = performance.now();
        try {
            return target.call(this, ...args);
        } finally {
            console.log(`${nom} : ${(performance.now() - debut).toFixed(3)} ms`);
        }
    };
}

const enMajuscule = (texte: string): string => texte.charAt(0).toUpperCase() + texte.slice(1);

// 3. Décorateur de champ : transforme la valeur de l'INITIALISEUR du champ
function capitalize(_valeur: undefined, _contexte: ClassFieldDecoratorContext) {
    return function (valeurInitiale: string): string {
        return enMajuscule(valeurInitiale);
    };
}

class Book {
    @capitalize
    title = "le petit prince"; // l'initialiseur est transformé : "Le petit prince"

    constructor(public readonly author: string) {}

    @logExecutionTime
    getBookInfo(): string {
        return `${this.title}, de ${this.author}`;
    }
}

// 🟣 Bonus : `accessor` + décorateur d'accesseur, pour transformer aussi les valeurs
// AFFECTÉES plus tard (dans le constructeur, par exemple)
function capitalizeAccessor<This>(
    cible: ClassAccessorDecoratorTarget<This, string>,
    _contexte: ClassAccessorDecoratorContext<This, string>,
): ClassAccessorDecoratorResult<This, string> {
    return {
        set(valeur: string) {
            cible.set.call(this, enMajuscule(valeur));
        },
    };
}

class Auteur {
    @capitalizeAccessor
    accessor nom: string;

    constructor(nom: string) {
        this.nom = nom; // passe par le setter décoré
    }
}

const livre = new Book("Saint-Exupéry");
console.log(livre.getBookInfo()); // Le petit prince, de Saint-Exupéry
console.log(new Auteur("hugo").nom); // Hugo
```

> ℹ️ Avec les décorateurs standard, un décorateur reçoit `(valeur, contexte)`. Un décorateur de **champ** reçoit `undefined` comme valeur et renvoie une fonction qui transforme la valeur initiale : **seule la valeur de l'initialiseur** (`title = "..."`) est concernée, pas celle affectée plus tard dans le constructeur. Pour intercepter aussi les affectations, utilisez le mot-clé `accessor` avec un décorateur d'accesseur (version bonus).

**Partie B : décorateurs historiques (`experimentalDecorators`)**

`tsconfig.json` (copie du projet) :

```json
{
    "compilerOptions": {
        "experimentalDecorators": true
    }
}
```

```ts
// fichier: legacy/ex22-param.ts
// 5. Décorateur de paramètre (n'existe que dans l'ancien système)
function LogParam(_cible: object, nomMethode: string | symbol, indice: number): void {
    console.log(`Paramètre n°${indice} de la méthode « ${String(nomMethode)} » décoré`);
}

class Service {
    saluer(@LogParam nom: string, @LogParam politesse: boolean): string {
        return politesse ? `Bonjour ${nom}` : `Salut ${nom}`;
    }
}

console.log(new Service().saluer("Alice", true));
// Paramètre n°1 de la méthode « saluer » décoré
// Paramètre n°0 de la méthode « saluer » décoré
// Bonjour Alice
```

> 💡 Les paramètres sont décorés **de droite à gauche** (d'où l'ordre ci-dessus), et au moment de la **définition** de la classe, pas de l'appel.

---

# Partie 8 : web et frameworks

## Exercice 23 : manipuler le DOM

`index.html` :

```html
<!DOCTYPE html>
<html lang="fr">
<body>
    <form id="formulaire">
        <input type="text" id="texte" placeholder="Votre texte" />
        <button type="submit">Envoyer</button>
    </form>
    <p>Aperçu : <span id="apercu"></span></p>
    <script type="module" src="/src/main.ts"></script>
</body>
</html>
```

```ts
// fichier: src/dom/main.ts
// @norun
// Nécessite "lib": ["ES2023", "DOM"]

// Récupère un élément, vérifie sa présence ET son type
function trouver<T extends HTMLElement>(id: string, type: new () => T): T {
    const element = document.getElementById(id); // type : HTMLElement | null
    if (!(element instanceof type)) {
        throw new Error(`Élément #${id} introuvable ou de mauvais type`);
    }
    return element;
}

try {
    const formulaire = trouver("formulaire", HTMLFormElement);
    const champ = trouver("texte", HTMLInputElement);
    const apercu = trouver("apercu", HTMLSpanElement);

    formulaire.addEventListener("submit", (event: SubmitEvent) => {
        event.preventDefault(); // empêche le rechargement de la page
        console.log("Valeur envoyée :", champ.value);
    });

    champ.addEventListener("input", () => {
        apercu.textContent = champ.value; // aperçu en temps réel
    });
} catch (e: unknown) {
    console.error(e instanceof Error ? e.message : e);
}
```

> 💡 `instanceof` fait deux choses d'un coup : il **vérifie à l'exécution** que l'élément existe et a le bon type, et il **rétrécit** le type pour le compilateur (plus besoin de `as`).

## Exercice 24 : frameworks

**⚛️ React : `src/App.tsx`**

```tsx
// fichier: src/App.tsx
// @norun
import { useState } from "react";

interface AppProps {
    name: string;
}

export default function App({ name }: AppProps) {
    const [greeting, setGreeting] = useState<string>("Bonjour");

    return (
        <div>
            <h1>
                {greeting}, {name} !
            </h1>
            <button onClick={() => setGreeting("Salut")}>Changer le message</button>
        </div>
    );
}
```

**🅰️ Angular : `message.service.ts` et `message.component.ts`**

```ts
// fichier: src/angular/message.service.ts
// @norun
import { Injectable } from "@angular/core";

@Injectable({ providedIn: "root" })
export class MessageService {
    private readonly messages: string[] = [];

    add(message: string): void {
        this.messages.push(message);
    }

    getAll(): readonly string[] {
        return this.messages;
    }
}
```

```ts
// fichier: src/angular/message.component.ts
// @norun
import { Component, input } from "@angular/core";

@Component({
    selector: "app-message",
    // `standalone: true` est la valeur par défaut depuis Angular 19
    standalone: true,
    template: `<p>{{ message() }}</p>`,
})
export class MessageComponent {
    // Entrée obligatoire, à base de signals ; on la lit en l'appelant : message()
    readonly message = input.required<string>();
}
```

**💚 Vue : `Compteur.vue`**

```vue
<script setup lang="ts">
import { ref } from "vue";

const message: string = "Bonjour depuis Vue";
const count = ref<number>(0);

function increment(): void {
    count.value++;
}
</script>

<template>
    <p>{{ message }}</p>
    <button @click="increment">Cliqué {{ count }} fois</button>
</template>
```

> 💡 Pour recevoir le message depuis un composant parent : `const props = defineProps<{ message: string }>();`.

## Exercice 25 : Express et NestJS

**Express 5 : `src/app.ts`**

```ts
// fichier: src/express/app.ts
import express, { type NextFunction, type Request, type Response } from "express";

const app = express();

app.get("/hello", (_req: Request, res: Response) => {
    res.send("Bonjour, TypeScript avec Express !");
});

app.get("/erreur", () => {
    throw new Error("Une erreur volontaire");
});

// Middleware d'erreurs : reconnu par Express grâce à ses QUATRE paramètres
app.use((err: Error, _req: Request, res: Response, _next: NextFunction) => {
    console.error(err.message);
    res.status(500).json({ error: err.message });
});

const serveur = app.listen(3456, async () => {
    const hello = await (await fetch("http://localhost:3456/hello")).text();
    const erreur = await (await fetch("http://localhost:3456/erreur")).json();
    console.log(hello, erreur); // Bonjour, TypeScript avec Express ! { error: 'Une erreur volontaire' }
    serveur.close();
});
```

```bash
npm install express
npm install --save-dev @types/express
```

> ℹ️ Avec Express 5, une route `async` qui rejette sa promesse est **automatiquement** transmise au middleware d'erreurs (avec Express 4, il fallait `try`/`catch` + `next(err)`).

**NestJS**

```ts
// fichier: src/nest/create-user.dto.ts
// @norun
import { IsEmail, IsString } from "class-validator";

export class CreateUserDto {
    @IsString()
    name!: string;

    @IsEmail()
    email!: string;
}
```

```ts
// fichier: src/nest/users.controller.ts
// @norun
import { Body, Controller, Post } from "@nestjs/common";
import { CreateUserDto } from "./create-user.dto.js";

@Controller("users")
export class UsersController {
    @Post()
    create(@Body() dto: CreateUserDto): { message: string } {
        return { message: `Utilisateur ${dto.name} créé avec succès` };
    }
}
```

```ts
// fichier: src/nest/main.ts
// @norun
import { ValidationPipe } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import { AppModule } from "./app.module.js";

const app = await NestFactory.create(AppModule);
app.useGlobalPipes(new ValidationPipe()); // rejette (400) les corps qui ne respectent pas le DTO
await app.listen(3000);
```

> ⚠️ NestJS repose sur l'ancien système de décorateurs : activez `experimentalDecorators` et `emitDecoratorMetadata` dans son `tsconfig.json` (le générateur `nest new` le fait pour vous).

---

# Partie 9 : données et tests

## Exercice 26 : accès aux données

> 🔐 Les URL de connexion viennent de variables d'environnement (`.env`, jamais versionné).

**MongoDB (Mongoose)**

```ts
// fichier: src/db/mongo.ts
// @norun
import mongoose, { Schema, model } from "mongoose";

interface IProduct {
    name: string;
    price: number;
    category: string;
}

const productSchema = new Schema<IProduct>({
    name: { type: String, required: true },
    price: { type: Number, required: true, min: 0 },
    category: { type: String, required: true },
});

const Product = model<IProduct>("Product", productSchema);

await mongoose.connect(process.env.MONGODB_URI ?? "mongodb://localhost:27017/boutique");

const cree = await Product.create({ name: "Stylo", price: 2.5, category: "papeterie" }); // Create
const lu = await Product.findById(cree._id); // Read
console.log(lu?.name);
await Product.updateOne({ _id: cree._id }, { price: 3 }); // Update
await Product.deleteOne({ _id: cree._id }); // Delete

await mongoose.disconnect();
```

**PostgreSQL (`pg`)**

```ts
// fichier: src/db/postgres.ts
// @norun
import pg from "pg";

interface Book {
    id: number;
    title: string;
    author: string;
    year_published: number;
}

const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });

await pool.query(`
    CREATE TABLE IF NOT EXISTS book (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year_published INT
    )`);

// Requêtes PARAMÉTRÉES ($1, $2…) : jamais de concaténation de texte (injection SQL)
const { rows } = await pool.query<Book>(
    "INSERT INTO book (title, author, year_published) VALUES ($1, $2, $3) RETURNING *",
    ["Dune", "Herbert", 1965],
);
const livre = rows[0];
if (livre) {
    console.log((await pool.query<Book>("SELECT * FROM book WHERE id = $1", [livre.id])).rows[0]);
    await pool.query("UPDATE book SET year_published = $1 WHERE id = $2", [1966, livre.id]);
    await pool.query("DELETE FROM book WHERE id = $1", [livre.id]);
}

await pool.end();
```

**TypeORM**

```ts
// fichier: src/db/typeorm.ts
// @norun
import "reflect-metadata";
import { Column, DataSource, Entity, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class Customer {
    @PrimaryGeneratedColumn()
    id!: number;

    @Column()
    name!: string;

    @Column({ unique: true })
    email!: string;

    @Column({ nullable: true })
    phone?: string;
}

const source = new DataSource({
    type: "postgres",
    url: process.env.DATABASE_URL,
    entities: [Customer],
    synchronize: true, // pratique en développement ; à proscrire en production (utiliser des migrations)
});
await source.initialize();

const depot = source.getRepository(Customer);
const client = await depot.save(depot.create({ name: "Alice", email: "alice@example.com" })); // Create
console.log(await depot.findOneBy({ id: client.id })); // Read
await depot.update(client.id, { phone: "0600000000" }); // Update
await depot.delete(client.id); // Delete

await source.destroy();
```

**➕ Bonus : Prisma** (typage généré à partir du schéma)

```prisma
// prisma/schema.prisma
model Customer {
  id    Int     @id @default(autoincrement())
  name  String
  email String  @unique
  phone String?
}
```

```ts
// fichier: src/db/prisma.ts
// @norun
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();
const client = await prisma.customer.create({ data: { name: "Alice", email: "alice@example.com" } });
// `client.nom` serait une erreur de compilation : les champs viennent du schéma
console.log(client.name);
```

> 💡 Avec Prisma ou Drizzle, le **type du résultat dépend de la requête** (`select`, `include`) : TypeScript détecte l'usage d'un champ non chargé, ce que `pg` ne peut pas faire.

## Exercice 27 : tests automatisés

**La fonction et la classe testées**

```ts
// fichier: src/tests/multiply.ts
export function multiply(a: number, b: number): number {
    return a * b;
}
```

```ts
// fichier: src/tests/bankAccount.ts
export class BankAccount {
    private _balance = 0;

    get balance(): number {
        return this._balance;
    }

    deposit(amount: number): void {
        if (amount <= 0) throw new Error("Le montant doit être positif");
        this._balance += amount;
    }

    withdraw(amount: number): void {
        if (amount <= 0) throw new Error("Le montant doit être positif");
        if (amount > this._balance) throw new Error("Solde insuffisant");
        this._balance -= amount;
    }
}
```

```ts
// fichier: src/tests/lireFichier.ts
import fs from "node:fs";

// Fonction à tester avec un faux système de fichiers
export function compterLignes(chemin: string): number {
    return fs.readFileSync(chemin, "utf-8").split("\n").filter((ligne) => ligne !== "").length;
}
```

**1. Jest** (avec `ts-jest` ou `@swc/jest`)

```ts
// fichier: src/tests/multiply.jest.test.ts
// @norun
import { multiply } from "./multiply";

describe("multiply", () => {
    it("multiplie des nombres positifs", () => {
        expect(multiply(3, 4)).toBe(12);
    });
    it("gère les nombres négatifs", () => {
        expect(multiply(-3, 4)).toBe(-12);
        expect(multiply(-3, -4)).toBe(12);
    });
    it("renvoie 0 avec zéro", () => {
        expect(multiply(0, 99)).toBe(0);
    });
});
```

**2. Mocha et Chai**

```ts
// fichier: src/tests/bankAccount.mocha.test.ts
// @norun
import { expect } from "chai";
import { BankAccount } from "./bankAccount.js";

describe("BankAccount", () => {
    let compte: BankAccount;
    beforeEach(() => {
        compte = new BankAccount(); // un compte neuf avant chaque test
    });

    it("met à jour le solde après un dépôt", () => {
        compte.deposit(100);
        expect(compte.balance).to.equal(100);
    });
    it("met à jour le solde après un retrait", () => {
        compte.deposit(100);
        compte.withdraw(30);
        expect(compte.balance).to.equal(70);
    });
    it("refuse un retrait supérieur au solde", () => {
        compte.deposit(10);
        expect(() => compte.withdraw(50)).to.throw("Solde insuffisant");
    });
});
```

**3. Simulation (*mock*) de `readFileSync`**

```ts
// fichier: src/tests/lireFichier.jest.test.ts
// @norun
import fs from "node:fs";
import { compterLignes } from "./lireFichier";

it("compte les lignes sans lire de vrai fichier", () => {
    const espion = jest.spyOn(fs, "readFileSync").mockReturnValue("a\nb\nc\n");
    expect(compterLignes("faux.txt")).toBe(3);
    expect(espion).toHaveBeenCalledWith("faux.txt", "utf-8");
    espion.mockRestore();
});
```

```ts
// fichier: src/tests/lireFichier.mocha.test.ts
// @norun
import { expect } from "chai";
import fs from "node:fs";
import sinon from "sinon";
import { compterLignes } from "./lireFichier.js";

describe("compterLignes", () => {
    afterEach(() => sinon.restore());

    it("compte les lignes sans lire de vrai fichier", () => {
        sinon.stub(fs, "readFileSync").returns("a\nb\nc\n");
        expect(compterLignes("faux.txt")).to.equal(3);
    });
});
```

**4. ➕ Lanceur intégré à Node.js : `node:test`** (aucune dépendance)

```ts
// fichier: src/tests/multiply.node.test.ts
import assert from "node:assert/strict";
import fs from "node:fs";
import { describe, it } from "node:test";
import { BankAccount } from "./bankAccount.js";
import { compterLignes } from "./lireFichier.js";
import { multiply } from "./multiply.js";

describe("multiply", () => {
    it("gère positifs, négatifs et zéro", () => {
        assert.equal(multiply(3, 4), 12);
        assert.equal(multiply(-3, 4), -12);
        assert.equal(multiply(0, 99), 0);
    });
});

describe("BankAccount", () => {
    it("refuse un retrait supérieur au solde", () => {
        const compte = new BankAccount();
        compte.deposit(10);
        assert.throws(() => compte.withdraw(50), /Solde insuffisant/);
    });
});

describe("compterLignes", () => {
    it("fonctionne avec un faux fichier", (t) => {
        t.mock.method(fs, "readFileSync", () => "a\nb\nc\n");
        assert.equal(compterLignes("faux.txt"), 3);
    });
});

```

```bash
node --import tsx --test src/tests/multiply.node.test.ts
```

> ✅ **Avantages de `node:test` / Vitest sur Jest** : aucune configuration de transformation (Vitest et `tsx` comprennent TypeScript et les modules ES nativement), démarrage plus rapide, et pour `node:test`, zéro dépendance. Jest reste très répandu, mais sa prise en charge des modules ES demande davantage de configuration.

---

## 🧾 Récapitulatif

| Partie | Notions démontrées |
| --- | --- |
| 1 | Inférence, tuples, `enum` contre `as const`, unions discriminées, exhaustivité (`never`), surcharges |
| 2 | `abstract`, `override`, propriétés de paramètre, contraintes génériques, `keyof`, mixins |
| 3 | `Partial`/`Pick`/`Omit`/`Record`, `DeepReadonly`, types mappés et conditionnels, `unknown` et gardes, `satisfies`, types gabarits |
| 4 | Validation de données non fiables, `??`, classe d'erreur personnalisée, déstructuration de tuples |
| 5 | `Promise.all` / `allSettled` / `race`, délai maximal, `unknown` dans `catch` |
| 6 | Modules ES, `namespace` historique, `.d.ts`, alias de chemins |
| 7 | Décorateurs standard et historiques |
| 8 | DOM typé, React/Angular/Vue, Express 5, NestJS |
| 9 | CRUD typé, requêtes paramétrées, `node:test`, mocks |
