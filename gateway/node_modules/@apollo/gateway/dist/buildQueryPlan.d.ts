import { DocumentNode } from 'graphql';
import { QueryPlan, OperationContext, WasmPointer } from './QueryPlan';
import { ComposedGraphQLSchema } from '@apollo/federation';
export interface BuildQueryPlanOptions {
    autoFragmentization: boolean;
}
export declare function buildQueryPlan(operationContext: OperationContext, options?: BuildQueryPlanOptions): QueryPlan;
interface BuildOperationContextOptions {
    schema: ComposedGraphQLSchema;
    operationDocument: DocumentNode;
    operationString: string;
    queryPlannerPointer: WasmPointer;
    operationName?: string;
}
export declare function buildOperationContext({ schema, operationDocument, operationString, queryPlannerPointer, operationName, }: BuildOperationContextOptions): OperationContext;
export {};
//# sourceMappingURL=buildQueryPlan.d.ts.map